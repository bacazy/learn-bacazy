# -*- coding: utf-8 -*-
import pickle
import time

from xrd.utils.constant import *
from xrd.utils.pipeline import pipeline


def currentTime():
    return time.asctime(time.localtime(time.time()))


def dump(fname, obj):
    with open(fname, 'wb') as fp:
        pickle.dump(obj, fp)
        fp.close()


def load(fname):
    with open(fname, 'rb') as fp:
        obj = pickle.load(fp)
        fp.close()
        return obj


if __name__ == '__main__':
    dump('x.j', {"asdasd": "中访问"})
    x = load('x.j')
    print(x['asdasd'])
