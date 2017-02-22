#coding:utf-8

import rarfile
import os
import re

def readRar(path, password=''):
    rarName = os.path.splitext(os.path.split(path)[1])[0]
    with rarfile.RarFile(path) as rf:
        if len(password) > 0:
            rf.setpassword(password)
        return rf.read(rarName + '.txt').decode('gbk')

def findShareLinkAndPwd(path):
    return re.findall(ur'百度云链接：(\S*)\s*密码：(\S{4})', readRar(path, 'bhdp'))

def saveFuliToBaiduPan(path):
    url, pwd = findShareLinkAndPwd(path)[0]
    print url, pwd
    os.system('python iScript/pan.baidu.com.py s ' + url + ' / -s ' + pwd)

def findFuli(dir):
    for rt, dirs, files in os.walk(dir):
        for f in files:
            print f
            saveFuliToBaiduPan(os.path.join(rt,f))

findFuli('data/')
