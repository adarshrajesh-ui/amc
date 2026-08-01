"""Provenance sweep v2: paced multi-engine, retries across passes, persistent store."""
import json, os, re, sys, time, urllib.parse
import search, phrases, net

HERE = os.path.dirname(os.path.abspath(__file__))
VENDOR = ['jobtestprep', 'quantblueprint', 'tradermath', 'tradinginterview', 'everythingquant',
          'theinterviewden', 'techinterview.org', 'howtoanalyzedata', 'programhelp.net', 'prepfully',
          'interviewquery', 'tryexponent', 'quantt.co.uk', 'scoutify', 'learncswithus',
          'interviews.chat', 'quantgrind', 'beyz', 'thewallstreetquants', 'peakframeworks',
          'quantguide', 'quantquestions', 'prepinsta', 'graduatesfirst', 'practiceaptitudetests',
          'assessment-training', 'wikijob', 'interviewkickstart', 'ambitionbox', 'preplounge',
          'quantinsti', 'wallstreetprep', 'interviewbit', 'simplilearn', 'careercup',
          'geeksforgeeks', 'faceprep', 'talentbattle', 'testpartnership', 'aonhewitt',
          'mconsultingprep', 'quantsprep', 'brainstellar', 'gradcracker', 'jobtestprep']
HOMEWORK = ['chegg', 'coursehero', 'numerade', 'brainly', 'gauthmath', 'quizlet', 'studocu',
            'bartleby', 'transtutors', 'doubtnut', 'toppr', 'vaia.com', 'studysmarter',
            'homeworklib', 'slader', 'symbolab', 'sladerx']
BOOKS = ['green book', 'xinfeng', 'heard on the street', 'crack', 'mark joshi', 'mosteller',
         'fifty challenging', '50 challenging', 'practical guide to quantitative']
CANDIDATE = ['reddit.com', 'teamblind.com', 'wallstreetoasis.com', '1point3acres', 'nowcoder',
             'yingjiesheng', 'quantnet.com', 'elitetrader', 'trade2win', 'thestudentroom',
             'glassdoor', 'indeed.com', 't.me', 'xiaohongshu', 'zhihu', 'github.com',
             'levels.fyi', 'blind']
MATHSITE = ['math.stackexchange', 'mathoverflow', 'puzzling.stackexchange', 'stackoverflow',
            'artofproblemsolving', 'aops', 'mathworld', 'oeis.org', 'wikipedia',
            'cut-the-knot', 'projecteuler', 'codeforces', 'leetcode']


def classify(u):
    lu = u.lower()
    t = []
    for v in VENDOR:
        if v in lu: t.append('vendor:' + v); break
    for hcat in HOMEWORK:
        if hcat in lu: t.append('homework:' + hcat); break
    for b in BOOKS:
        if b.replace(' ', '-') in lu or b.replace(' ', '') in lu: t.append('book:' + b); break
    for m in MATHSITE:
        if m in lu: t.append('math:' + m); break
    for c in CANDIDATE:
        if c in lu: t.append('cand:' + c); break
    return t or ['other']


def queries_for(rec):
    q = rec.get('question_text') or ''
    qen = rec.get('question_text_en') or ''
    out = []
    if phrases.is_cjk(q):
        p = phrases.cjk_phrase(q, 14)
        if p: out.append('"%s"' % p)
        if qen:
            pe = phrases.distinctive(qen, 10)
            if pe: out.append('"%s"' % pe)
    else:
        p = phrases.distinctive(q, 11)
        if p: out.append('"%s"' % p)
        p8 = phrases.distinctive(q, 7)
        if p8 and p8 != p: out.append('"%s"' % p8)
    return out[:2]


def main():
    recs = {}
    for l in open(os.path.join(HERE, '..', 'questions.jsonl')):
        r = json.loads(l); recs[r['id']] = r
    ids = json.load(open(sys.argv[1]))
    outp = sys.argv[2]
    passes = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    res = {}
    if os.path.exists(outp):
        res = json.load(open(outp))
    for p in range(passes):
        pending = 0
        for i in ids:
            r = recs.get(i)
            if not r: continue
            cur = res.setdefault(i, {'id': i, 'queries': {}})
            for q in queries_for(r):
                if q in cur['queries'] and cur['queries'][q].get('ok'):
                    continue
                sr = search.search(q)
                cur['queries'][q] = {'ok': sr['ok'], 'engine': sr['engine'],
                                     'links': sr['links'][:15],
                                     'tags': sorted({t for u in sr['links'][:15] for t in classify(u)})}
                if not sr['ok']:
                    pending += 1
                json.dump(res, open(outp, 'w'))
        print('pass %d done, unresolved=%d' % (p, pending), flush=True)
        if pending == 0:
            break
        time.sleep(20)
    json.dump(res, open(outp, 'w'))
    print('FINISHED', len(res))


if __name__ == '__main__':
    main()
