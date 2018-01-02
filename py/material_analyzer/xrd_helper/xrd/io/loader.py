# -*- coding: utf-8 -*-
import numpy as np

from xrd.backend import Xrd


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
