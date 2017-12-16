# -*- coding: utf-8 -*-
from xrd.misc.xrd import Xrd
import numpy as np


def loadtxt(fname):
    f_data = np.loadtxt(fname=fname, dtype=float, skiprows=1)
    xrd = Xrd()
    xrd.fname = fname
    xrd.theta = f_data[:, 0]
    xrd.intensity = f_data[:, 1]
    return xrd


def load(fname, ftype='txt'):
    if ftype == 'txt':
        return loadtxt(fname)
    else:
        raise Exception(ftype + " is not supported now")
