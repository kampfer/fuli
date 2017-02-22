#coding:utf-8

import requests
import re
from urlparse import urljoin
import pickle
import time

host = 'http://bhdp1.over-blog.com'
next =urljoin(host, '/page/1')
s = requests.session()
fuli = []
while next:
    print next
    page = s.get(next)
    fuli.extend(re.findall(ur'\(链接复制打开\)百度云下载地址：\s*(\S*)', page.text))
    next = re.findall(ur'<a\s+href="(\S*)"\s+class="ob-page ob-page-link ob-page-next"\s+>></a>', page.text)
    if len(next) > 0:
        next = urljoin(host, next[0])
    else:
        next = ''
        print 'done'

f = open(time.strftime("%Y%m%d%H%M%S", time.localtime()), 'wb')
pickle.dump(set(fuli), f)
f.close()
