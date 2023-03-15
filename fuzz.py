#!/usr/bin/python3

import sys
from itertools import product
from multiprocessing import Pool

import util.fuzz as fuzz
from util import cmd, pprint, execute
from const import PARSERS, REQUESTERS

DEBUG = 'debug' in sys.argv

INS_COUNT = [0, 3, 0]
WHITELIST = ['127.0.0.1', '127.1.1.1', '127.2.2.2', '127.1.1.1\n127.2.2.2']
CHARSETS = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0cA01\x00'
FORMAT = 'http://{0}127.1.1.1{1}127.2.2.2{2}'.format('{}' * INS_COUNT[0], '{}' * INS_COUNT[1], '{}' * INS_COUNT[2])

def _print(msg):
    sys.stdout.write("%s\n" % msg)

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

def run(random_data):
    url = FORMAT.format(*random_data)
    url = url + '/' + (''.join(random_data).encode('hex'))
    url = url.replace('\x00', '%00')

    urls = run_parser(url)
    gets = run_requester(url)

    total_urls = {}
    for k,v in urls.iteritems():

        # filter
        if v not in WHITELIST:
            continue

        if total_urls.get(v):
            total_urls[v].append(k)
        else:
            total_urls[v] = [k]

    if len(total_urls) > 1:
        msg = 'parsed url = {0}\n'.format(url)
        for k, v in sorted(total_urls.iteritems(), key=lambda x: len(x[1]), reverse=True):
            msg += '{0:<16} {1} = {2}\n'.format(k, len(v), repr(v))

        _print(msg)


    total_gets = {}
    for k, v in gets.iteritems():
        v = v.split('/')[0]

        # filter
        if v == 'err':
            continue

        if total_gets.get(v):
            total_gets[v].append(k)
        else:
            total_gets[v] = [k]

    if len(total_gets) > 1:
        msg = 'got url = {0}\n'.format(url)
        for k, v in sorted(total_gets.iteritems(), key=lambda x: len(x[1]), reverse=True):
            msg += '{0:<24} {1} = {2}\n'.format(k, len(v), repr(v))
        _print(msg)


data_set = product(list(CHARSETS), repeat=sum(INS_COUNT))
if DEBUG:
    for i in data_set: run(i)
else:
    pool = Pool(32)
    result = pool.map_async(run, data_set).get(0xfffff)
