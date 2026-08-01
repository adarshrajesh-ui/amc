#!/usr/bin/env python3
"""Assemble reports/independent_verification.json from the per-record adjudications.

Every verdict below was reached by fetching the cited URL over a network path that
does not go through this machine's plain-Python client (WebFetch, the r.jina.ai text
proxy, the Arctic Shift Reddit archive, the search tool's page fetcher, or a Wayback
snapshot), then comparing the stored source_quote against the retrieved page text with
whitespace and full-width punctuation folded.
"""
import json
import re
from collections import Counter, OrderedDict, defaultdict

SEED = 42

# id -> (status, method, defect_class, note, firm_attribution)
V = {
    "51ca13558f45e3": (
        "UNCHECKABLE", "websearch", "none",
        "1point3acres tag/twosigma-1247-8.html could not be retrieved by any route (direct 403, "
        "r.jina.ai served the Cloudflare interstitial, no Wayback snapshot, and the search tool "
        "would not fetch this tag page). Third-party writeups of the Two Sigma OA independently "
        "describe exactly this pair of tasks (a hand-rolled Linear Interpolator with no libraries, "
        "and an NYC temperature linear-regression task), so the content is plausible, but I did not "
        "see the cited preview row itself. Not evidence against the record.",
        "MISLABELLED: quote opens 'Two sigma 在线笔试题' and the URL is the Two Sigma tag page, "
        "but the record's firm is 'Susquehanna International Group'."),
    "c6553cd14443ae": (
        "PARTIAL", "websearch", "ellipsis_join",
        "The search tool fetched thread-1042392 and every fragment of the quote is present on the "
        "page, but not as one span: the stored quote welds together the OP's body, a bracketed "
        "rewrite of the 188-point paywall banner, the orphan formula fragment '/3*C^2_n', and two "
        "later replies (匿名用户 2024-2-5, 猫咪猫咪爪 2024-02-18), separated by ' ... '. Genuine text, "
        "non-contiguous assembly.", None),
    "b8ef9bd2d15845": (
        "CONFIRMED", "webfetch", "none",
        "teamblind.com is directly reachable from this host. 'Their OA questions felt like LC "
        "mediums (?) . Any insights into what to expect and focus on while preparing?' appears "
        "verbatim in the OP of the post titled 'Two Sigma Interview prep'.",
        "MISLABELLED: the post is about Two Sigma; the record's firm is 'Susquehanna International Group'."),
    "2bc6cbab1fcad3": (
        "CONFIRMED", "webfetch", "none",
        "'How to implement Huffman coding trees.' is the entire Questions section of the jointaro "
        "experience page, dated October 1, 2018, matching the record's post_date.",
        "MISLABELLED: the jointaro page is under /companies/two-sigma/; the record's firm is "
        "'Susquehanna International Group'."),
    "8caedcd978cbcd": (
        "CONFIRMED", "webfetch", "none",
        "Fetched t.me/s/usinterview/29040 and isolated the single message. The quote is verbatim in "
        "the message's 1point3acres link-preview description. Note the quote is the preview of the "
        "linked thread, not the Telegram poster's own words - which the record's doubt field states.",
        "MISLABELLED: the message is tagged #twosigma and links a Two Sigma thread; the record's "
        "firm is 'Susquehanna International Group'."),
    "863ed94f6a4f5d": (
        "CONFIRMED", "webfetch", "none",
        "Verbatim contiguous substring of the link-preview text on t.me/usinterview/19241 "
        "('SIG QR 17题OA', tagged #sig). The stored quote starts mid-sentence at 求绿色三角形的重量, "
        "dropping the leading 新题库…感觉还挺难的…, but everything kept is contiguous.", None),
    "cc591e97228419": (
        "CONFIRMED", "webfetch", "none",
        "Present verbatim, emoji included, at line 713 of public/docs/game_theory_sig.html in "
        "ldvyyc/InterviewPrep. This is a third-party study compilation, not first-person recall - "
        "the record marks access as compilation_only.", None),
    "d246abad8571a8": (
        "UNCHECKABLE", "websearch", "none",
        "Glassdoor review permalink RVW104274099 unreachable: direct fetch 403, WebFetch hit the "
        "Cloudflare 'Humans only' page, r.jina.ai's free quota was exhausted mid-run, no Wayback "
        "snapshot exists for the permalink, and the search tool returned the aggregate listing "
        "instead. Note for follow-up: 'a fifty question aptitude test' is unusual against SIG's "
        "widely reported 9-20 question assessments, so this one is worth re-checking - but I could "
        "not reach the page, so this is not evidence against the record.", None),
    "a0d52d06d56471": (
        "UNCHECKABLE", "websearch", "none",
        "Glassdoor review permalink RVW12633809 (Nov 2016) unreachable by the same four routes. "
        "Corroborating but not confirming: the Glassdoor SIG Quantitative Trader listing page, which "
        "the search tool did fetch, carries a closely related painting/expected-value review, so the "
        "question family is real on Glassdoor for SIG.", None),
    "58a7b7f20d6ec5": (
        "CONFIRMED", "webfetch", "none",
        "Retrieved via the r.jina.ai text proxy. 100% verbatim, including the collector's convention "
        "of serialising Glassdoor's rendered labels ('Interview' / 'Interview questions [1]' / "
        "'Question 1') into the quote - that is a faithful reading-order capture, not a join. Review "
        "dated Nov 11, 2024, matching the record's post_date.", None),
    "a73ac695055f4d": (
        "CONFIRMED", "webfetch", "none",
        "Reddit blocks this host and WebFetch, so I read comment m7xybti from the Arctic Shift public "
        "Reddit archive. body matches 100%, author n0obmaster699, link_id t3_1gr8l9m matching the "
        "post id in the cited URL.", None),
    "f82135488935d8": (
        "CONFIRMED", "webfetch", "none",
        "Arctic Shift comment i42romz by AnimalCandid823 under t3_tzyuhp: 100% match including the "
        "backslash-escaped markdown (a\\^2-\\`b\\^2) the collector preserved rather than cleaned up.", None),
    "763fa06c7247a2": (
        "PARTIAL", "wayback", "paraphrase",
        "Wayback snapshot 20250912084409 of thread-1144112 (GBK-encoded) contains the English "
        "question, 答案:62/77, and the Chinese explanation contiguously - 330 of 413 characters match "
        "as one span. The divergence is the equation line: the page renders MathJax twice as digit "
        "soup ('P3=23+13P1...P_3=\\frac{2}{3}...'), and the collector rewrote it as "
        "'P3=2/3+1/3·P1, ...'. Light editing of notation, no invented content. The record's own doubt "
        "field discloses precisely this reconstruction.", None),
    "a0bcca6b3398ae": (
        "CONFIRMED", "webfetch", "none",
        "Verbatim in the 'Junior Quant Researcher Interview - Quantitative Research' entry, Date "
        "Submitted Jan 14, 2026, matching the record's post_date. The entry is on page 1 of the cited "
        "aggregate listing, so citing the listing rather than a permalink is not a granularity defect here.",
        "MISLABELLED: the page is wallstreetoasis.com/company/two-sigma-investments/; the record's "
        "firm is 'Susquehanna International Group'."),
    "855e4f0bcedba3": (
        "CONFIRMED", "webfetch", "none",
        "Verbatim on the Software Engineering Intern permalink, interviewed February 2025, matching "
        "the record's post_date. The same submission also appears on the aggregate listing, which the "
        "record's doubt field already flags as a single account counted from two URLs.",
        "MISLABELLED: Two Sigma Investments page; the record's firm is 'Susquehanna International Group'."),
    "a251ce474a305f": (
        "CONFIRMED", "websearch", "none",
        "The search tool fetched the exact cited tag page and returned the preview row verbatim: "
        "'Brain teaser: It was like a coinflip and if u win u get $1, if u lose u lose $1, u have a "
        "slight edge int this game, would u play itobv if u have a slight edg ...', poster brawler1232 "
        "2024-9-26, matching the record's post_date. The stored quote is a clean prefix cut at "
        "'would u play it'. The row is still on page 3, so the re-ordering risk the record warned "
        "about has not bitten.", None),
    "36d7b6d1250340": (
        "UNCHECKABLE", "websearch", "none",
        "thread-934179 could not be retrieved: direct 403, no Wayback snapshot, r.jina.ai blocked by "
        "Cloudflare, and the search tool did not surface the page. Not evidence against the record.", None),
    "e53a4249b6b409": (
        "CONFIRMED", "wayback", "none",
        "Wayback snapshot 20231017071522 of thread-1022110 ('HRT Algo Dev OA'). Once the two '|' "
        "characters wrapping the stored quote are removed - they are markdown-table delimiters from "
        "the snippet extractor, not page content - the remaining 46 characters match contiguously. "
        "The quote does begin mid-word at 'ht的node' because the preceding text is behind the forum's "
        "188-point wall, which the record's doubt field states explicitly.", None),
    "3cbe6840048912": (
        "CONFIRMED", "webfetch", "none",
        "Verbatim in a comment on the Blind post 'DRW phone interview', dated Aug 31 2020 (the record "
        "says 2020-09-01, a timezone-width difference).", None),
    "2e2a23e6fed5d9": ("CONFIRMED", "webfetch", "none",
                       "Verbatim in the Round-1 narrative of the GeeksforGeeks D.E. Shaw 2023 experience.", None),
    "57513fe1137ff0": ("CONFIRMED", "webfetch", "none",
                       "题目6 on the CSDN post, verbatim including all five options A-E.", None),
    "93c9770cba46a6": ("CONFIRMED", "webfetch", "none",
                       "Verbatim in Round 2 of the GeeksforGeeks DE Shaw 2021 experience.", None),
    "53683aba125b15": ("CONFIRMED", "webfetch", "none",
                       "Verbatim in the 1st-round question list of the single Optiver interview review on canarywharfian.", None),
    "224c44de915eca": ("CONFIRMED", "webfetch", "none",
                       "Verbatim in the link-preview text of t.me/usinterview/20370 ('Jump 面试', #jumptrading).", None),
    "90475afdd1addc": ("CONFIRMED", "webfetch", "none",
                       "Verbatim in the link-preview text of t.me/usinterview/29079 ('HRT面筋', #hudson-river-trading).", None),
    "eecce57bfc3e9c": ("CONFIRMED", "webfetch", "none",
                       "Verbatim contiguous substring of the link-preview on t.me/usinterview/27543 ('简街onsite挂经'); "
                       "the quote ends where Telegram itself truncates the preview.", None),
    "c0e0e9e4ffe6eb": ("CONFIRMED", "webfetch", "none",
                       "Downloaded MW_Quant_Application_Guide.pdf (HTTP 200, 10 pages) and extracted the text: the "
                       "sentence appears verbatim, with the same 'i th' spacing the record preserves.", None),
    "8b33567e30f80a": ("CONFIRMED", "websearch", "none",
                       "The search tool fetched the exact cited URL; 'They ask me about data analysis, statistics and "
                       "coding questions.' appears verbatim in an Intern Interview review (London).", None),
    "6738b3c866f5b1": ("CONFIRMED", "websearch", "none",
                       "The search tool fetched the exact cited URL and returned 'Interview questions [1] ... Question 1 "
                       "... Probability and Game Theory, optimal strategy and the expected return' verbatim.", None),
    "a4b2a2f34feb69": ("CONFIRMED", "webfetch", "none",
                       "Verbatim in the 'Applied Scientist Interview - Infrastructure' entry, Date Submitted Dec 10, 2025, "
                       "matching the record's post_date.", None),
    "f1ea4994ada87d": ("CONFIRMED", "webfetch", "none",
                       "Verbatim in the 'Desk Quant Analyst Interview - Hedge Fund' entry, Date Submitted May 31, 2026, "
                       "matching the record's post_date.", None),
    "bc90debb94c093": ("CONFIRMED", "webfetch", "none",
                       "Verbatim in the 'Trade Operation Analyst Interview - Operations' entry, Date Submitted Apr 13, 2025, "
                       "matching the record's post_date.", None),
    "4471b3c8b600fe": ("CONFIRMED", "websearch", "none",
                       "The search tool fetched the exact cited URL and returned the sentence verbatim, including the "
                       "trailing 'number of gas stations in California' clause.", None),
    "1e442858bd831c": (
        "PARTIAL", "webfetch", "ellipsis_join",
        "nowcoder is directly reachable from this host. Both halves of the quote are genuine: the "
        "thread title 城堡hk量化实习两轮电面挂经 is on the page, and the 254-character body excerpt "
        "starting 二面是刚毕业的牛津数学phd matches contiguously. But they are not adjacent - the "
        "excerpt starts partway into the post - so the stored '# <title> <mid-body excerpt>' string "
        "never appears as one span.", None),
    "b17e606c8f4092": ("CONFIRMED", "webfetch", "none",
                       "Short quote (17 chars) present verbatim on the fetched nowcoder feed page.", None),
    "16e9bec76389b5": ("CONFIRMED", "webfetch", "none",
                       "Title and body are adjacent on the page, so the whole 384-character body plus title matches "
                       "contiguously; the only addition is the leading '# ' markdown heading marker.", None),
    "a6e874dd06850b": (
        "UNCHECKABLE", "websearch", "none",
        "thread-1141422 could not be retrieved (403 direct, no Wayback snapshot, jina blocked, search "
        "tool would not fetch it). Corroborating but not confirming: 1point3acres' own Optiver "
        "problem page independently lists 'Flip a coin 3 times - probability the outcome is the same "
        "for all flips? (0.25)' as an Optiver Beat-the-Odds item. Not evidence against the record.", None),
    "2befd908dd5790": ("CONFIRMED", "webfetch", "none",
                       "Arctic Shift comment g7h9nuq by 11AMBoi in the cited csMajors thread: 100% match.", None),
    "d08318ed15de86": ("CONFIRMED", "webfetch", "none",
                       "Arctic Shift comment p053dp8 by DeeplyEquable in the cited quantfinance thread: 100% match.", None),
    "cd510f6257b55f": ("CONFIRMED", "webfetch", "none",
                       "Verbatim in reply 5 of the thread. The '...' inside the quote is the poster's own ellipsis, "
                       "not a join.", None),
    "2c61b077347939": ("CONFIRMED", "webfetch", "none",
                       "Verbatim in the Aptitude Section bullet of the ecedplacement DE Shaw post.", None),
    "0d43aee4c7ba97": ("CONFIRMED", "webfetch", "none",
                       "Verbatim on the Junior Trader permalink, interviewed July 2025, matching the record's post_date - "
                       "including the poster's typos 'oculd', 'calulator', 'sceniors', which is strong evidence of "
                       "transcription rather than reconstruction.", None),
    "11d533c3cca8db": ("CONFIRMED", "webfetch", "none",
                       "Verbatim in the 'Algorithm Development Internship Interview' entry, Date Submitted Nov 10, 2022, "
                       "matching the record's post_date.", None),
    "468d20e956ab54": ("CONFIRMED", "webfetch", "none",
                       "Verbatim in the 'Quant Trader Interview' entry, Date Submitted Nov 15, 2024, matching the "
                       "record's post_date.", None),
    "5f1e42a6733de3": ("CONFIRMED", "webfetch", "none",
                       "Verbatim on the Quantitative Trader Intern permalink, interviewed August 2025.", None),
}


# The in-repo Python checker reported 18 FAIL/PARTIAL rows and those were handed to me as
# "18 genuine mismatches". They fall on three URLs, all of which I re-fetched myself over a
# path the checker did not have. Two of the three clusters turn out to be checker artefacts.
CHECKER_ADJUDICATION = OrderedDict([
    ("summary", "Of the 18 rows the in-repo checker flagged as mismatches, 14 are checker "
                "artefacts (the quotes are verbatim at the cited URL) and 4 are real "
                "ellipsis-join defects. None is invention."),
    ("clusters", [
        OrderedDict([
            ("source_url", "https://www.wallstreetoasis.com/company/susquehanna-international-group/interview"),
            ("checker_rows", 10),
            ("checker_reason", "quote_not_found, 2-17 chars matched, via wayback"),
            ("my_verdict", "FALSE ALARM - all 10 quotes are 100% verbatim on the live page"),
            ("explanation",
             "The checker is Cloudflare-blocked on wallstreetoasis.com so it fell back to a Wayback "
             "snapshot. The listing now holds 258 entries and the ten quotes come from five reviews "
             "dated 2025-09-07 to 2026-01-29, which postdate the snapshot it read. I re-fetched the "
             "live page through the r.jina.ai text proxy (73 KB) and every one of the ten quotes is "
             "a 100% verbatim contiguous substring."),
        ]),
        OrderedDict([
            ("source_url", "https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/SIG/Quantitative%20Trader%20-%202022%20Programme.md"),
            ("checker_rows", 4),
            ("checker_reason", "quote_not_found, 0 chars matched, via live"),
            ("my_verdict", "FALSE ALARM - all 5 quotes citing this file are 100% verbatim"),
            ("explanation",
             "A 0/349-character match on a reachable public file is the strongest fabrication signal "
             "in the whole corpus, so I checked it first. The checker fetched the github.com /blob/ "
             "URL, which is a JavaScript-rendered React shell containing none of the file body. "
             "Fetching the raw.githubusercontent.com equivalent (HTTP 200, 9802 bytes) shows all five "
             "attestations matching at 100%: 284/284, 217/217, 114/114, 242/242 and 450/450 chars."),
        ]),
        OrderedDict([
            ("source_url", "https://xjtu.app/t/topic/12756"),
            ("checker_rows", 4),
            ("checker_reason", "quote_not_found, 43-58% matched, via live"),
            ("my_verdict", "GENUINE DEFECT - ellipsis_join, but every segment is real page text"),
            ("explanation",
             "This host is not blocked, so the checker did read the real page. All four quotes break "
             "at exactly the ' ... ' marker. Splitting each quote on its ellipsis and testing the "
             "segments separately, all 9 segments across the 4 quotes are verbatim contiguous "
             "substrings of the page. The collector welded non-adjacent passages of one genuine post "
             "together; it did not write any of the text. In one case the second segment is also "
             "stored as its own standalone attestation, where it matches at 100%."),
        ]),
    ]),
])


def corpus_scan():
    """Whole-corpus counts for the three named defect classes, so the sample can be generalised."""
    recs = [json.loads(l) for l in open("/workspace/harvest/questions.jsonl") if l.strip()]
    atts = [(r, a) for r in recs for a in r.get("attestations", [])]
    n = len(atts)

    ell = [a for _, a in atts if a.get("source_quote") and re.search(r"(\s\.\.\.\s|…)", a["source_quote"])]
    agg_re = re.compile(r"(wallstreetoasis\.com/company/[^/]+/interview/?$|/bbs/tag/"
                        r"|glassdoor\.[a-z.]+/Interview/[^/]*-Interview-Questions-E\d+\.htm$)")
    agg = [a for _, a in atts if agg_re.search(a.get("source_url", ""))]

    sig = "Susquehanna International Group"
    sig_ids = {r["id"] for r in recs if r["firm"] == sig}
    mis = set()
    for r, a in atts:
        if r["firm"] != sig:
            continue
        blob = (a.get("source_url", "") + " " + (a.get("source_quote") or "") + " "
                + (a.get("poster_context") or "")).lower()
        if "two sigma" in blob or "twosigma" in blob or "two-sigma" in blob:
            mis.add(r["id"])

    return OrderedDict([
        ("records", len(recs)),
        ("attestations", n),
        ("distinct_source_urls", len({a.get("source_url") for _, a in atts})),
        ("ellipsis_join", OrderedDict([
            ("attestations", len(ell)), ("pct_of_attestations", round(100 * len(ell) / n, 1)),
            ("by_source_type", OrderedDict(sorted(Counter(a.get("source_type") for a in ell).items()))),
            ("note", "Quote contains ' ... ' or an ellipsis character joining passages. Where I could "
                     "test the segments (xjtu.app, 1point3acres, nowcoder) every segment was genuine "
                     "page text, so this is citation sloppiness, not invented content."),
        ])),
        ("wrong_granularity", OrderedDict([
            ("attestations", len(agg)), ("pct_of_attestations", round(100 * len(agg) / n, 1)),
            ("by_source_type", OrderedDict(sorted(Counter(a.get("source_type") for a in agg).items()))),
            ("note", "URL is an aggregate listing or tag page rather than a per-review permalink. This "
                     "is only a real defect once the entry scrolls off page 1: WSO and Glassdoor "
                     "listings render full review bodies inline, and in every sampled case the cited "
                     "entry was still present on the page I fetched."),
        ])),
        ("truncated_url", OrderedDict([
            ("attestations", 0),
            ("note", "Scanned all 813 distinct URLs for dangling hyphens/underscores, cut percent-"
                     "escapes, short Glassdoor RVW ids and clipped slugs. No instances found; this "
                     "defect class is absent from the corpus."),
        ])),
        ("firm_mislabel", OrderedDict([
            ("sig_labelled_records", len(sig_ids)),
            ("actually_two_sigma", len(mis)),
            ("pct_of_sig", round(100 * len(mis) / len(sig_ids), 1)),
            ("note", "'Two Sigma' does not exist as a firm value anywhere in the corpus (50 distinct "
                     "firms); its records were folded into 'Susquehanna International Group', "
                     "presumably by a normaliser matching on the token 'Sigma'. The quotes and URLs "
                     "are genuine - the attribution is wrong. 6 of my 45 sampled records hit this."),
        ])),
    ])


def main():
    sample = json.load(open("/workspace/harvest/reports/_sample45.json"))["sample"]
    assert set(V) == {s["id"] for s in sample}, "verdicts and sample must line up"

    results = []
    by_type = defaultdict(lambda: OrderedDict(
        [("CONFIRMED", 0), ("PARTIAL", 0), ("CONTRADICTED", 0), ("UNCHECKABLE", 0)]))
    for s in sample:
        status, method, defect, note, firm = V[s["id"]]
        row = OrderedDict([
            ("id", s["id"]), ("firm", s["firm"]), ("source_type", s["source_type"]),
            ("source_url", s["source_url"]), ("status", status), ("method", method),
            ("defect_class", defect), ("note", note),
        ])
        if firm:
            row["firm_attribution"] = firm
        results.append(row)
        by_type[s["source_type"]][status] += 1

    out = OrderedDict([
        ("sample_size", len(results)),
        ("seed", SEED),
        ("results", results),
        ("by_source_type", OrderedDict(sorted(by_type.items()))),
        ("checker_mismatch_adjudication", CHECKER_ADJUDICATION),
        ("corpus_defect_scan", corpus_scan()),
    ])
    path = "/workspace/harvest/reports/independent_verification.json"
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)

    tot = defaultdict(int)
    for r in results:
        tot[r["status"]] += 1
    print(f"wrote {path}")
    for k in ("CONFIRMED", "PARTIAL", "CONTRADICTED", "UNCHECKABLE"):
        print(f"  {k:13s} {tot[k]:3d}  {tot[k]/len(results):5.1%}")
    print("\nby source type:")
    print(f"  {'source_type':22s} {'CONF':>5} {'PART':>5} {'CONTRA':>7} {'UNCH':>5}  reliability")
    for st, c in sorted(by_type.items()):
        reached = c["CONFIRMED"] + c["PARTIAL"] + c["CONTRADICTED"]
        rel = f"{c['CONFIRMED']/reached:.0%} of {reached} reached" if reached else "n/a (none reached)"
        print(f"  {st:22s} {c['CONFIRMED']:5d} {c['PARTIAL']:5d} {c['CONTRADICTED']:7d} {c['UNCHECKABLE']:5d}  {rel}")
    print("\nmislabelled firm (source names a different firm than the record):")
    for r in results:
        if "firm_attribution" in r:
            print(f"  {r['id']}  {r['source_type']:14s} {r['source_url'][:78]}")


if __name__ == "__main__":
    main()
