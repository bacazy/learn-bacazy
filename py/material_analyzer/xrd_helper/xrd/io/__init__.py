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
        data = np.array(array)
        return {
            '2theta': data[:, 0],
            'd': data[:, 2],
            'Centroid': data[:, 4],
            'Height': data[:, 5],
            'Area': data[:, 7],
            'Shape': data[:, 10],
            'Skew': data[:, 11],
            'FWHM': data[:, 12],
            'Breadth': data[:, 14],
            'XS': data[:, 15],
        }


if __name__ == '__main__':
    print(loadfit(r'E:\laji\expriment\raw\XRD\20170527\2017052707\2017052707.fit', skiprows=10))
