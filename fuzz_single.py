#!/usr/bin/python3
import sys
from const import PARSERS, REQUESTERS

def run_parser(url):
    res = {}
    for key, binary in PARSERS.iteritems():
        lang, libname = key.split('.', 1)
        r = execute(lang, binary, url, base='bin/parser/')

        # parse host, change here to get the result you want
        if 'host=' in r and 'port=' in r:
            res[key] = r.split('host=')[-1].split(', ')[0]
        else:
            res[key] = 'err'

    return res

def run_requester(url):
    res = {}
    for key, binary in REQUESTERS.iteritems():
        lang, libname = key.split('.', 1)

        r = execute(lang, binary, url, base='bin/requester/')
        res[key] = r
    return res



urls = run_parser(sys.argv[1])
gets = run_requester(sys.argv[1])

total = {}
for k,v in urls.iteritems():
    if total.get(v):
        total[v].append(k)
    else:
        total[v] = [k]

print([sys.argv[1]])
print('[parsers]')
for k, v in sorted(total.iteritems(), key=lambda x: len(x[1]), reverse=True):
    print('{0:<24s} {1} = '.format([k], len(v)), v)

total = {}
for k,v in gets.iteritems():
    v = v.split('/')[0]
    if total.get(v):
        total[v].append(k)
    else:
        total[v] = [k]

print('\n[requesters]')
for k, v in sorted(total.iteritems(), key=lambda x: len(x[1]), reverse=True):
    print('{0:<24} {1} = '.format(k, len(v)), v)
print('')
