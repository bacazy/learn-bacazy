# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from xrd.backend.base import Xrd
import numpy as np
import re


def loadtxt(fname):
    f_data = np.loadtxt(fname=fname, dtype=float, skiprows=1)
    xrd = Xrd()
    xrd.fname = fname
    xrd.theta = f_data[:, 0]
    xrd.intensity = f_data[:, 1]
    return xrd


def load_xrdprj(fname):
    pass


def load(fname, ftype='txt'):
    if ftype == 'txt':
        return loadtxt(fname)
    if ftype == 'xrdprj':
        return load_xrdprj(fname)
    else:
        raise Exception(ftype + " is not supported now")


def loadfit(fname, skiprows=0):
    with open(fname) as fp:
        lines = fp.readlines()
        pa = re.compile(r'[-+]?[0-9]*\.?[0-9]+')
        array = []
        while skiprows < len(lines):
            line = lines[skiprows]
            splt = pa.findall(line)
            array.append([float(e) for e in splt])
            skiprows += 1
        return np.array(array)
