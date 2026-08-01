import net,re,json,os,time
from concurrent.futures import ThreadPoolExecutor
links=json.load(open('bs_links.json'))
def get(p):
    u='https://brainstellar.com'+p
    h=net.fetch(u,'bsp')
    t=re.sub(r'\s+',' ',net.strip_html(h))
    # strip the common nav chrome
    t=re.sub(r'^.*?Light Dark','',t)
    return {'url':u,'text':t[:4000]}
out=[]
with ThreadPoolExecutor(max_workers=8) as ex:
    for r in ex.map(get,links): out.append(r)
json.dump(out,open('brainstellar.json','w'))
print('scraped',len(out),'avg len',sum(len(o['text']) for o in out)//max(1,len(out)))
