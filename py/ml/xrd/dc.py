# -*- coding: utf-8 -*-
from xrd.analysis.dislocations import h2, C, K, dK
from xrd.io import loadfit
from xrd.data import FerriteMiller
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    aray = loadfit(r'E:\laji\expriment\raw\XRD\20171226\20171226-4\20171226-4.fit', 10)
    peaks = aray[:, 0]
    fwhms = aray[:, 12]
    for q in [2]:
        k2c = []
        dk = []
        for i in range(len(peaks)):
            hkl = FerriteMiller[i]
            peak = peaks[i]
            fwhm = fwhms[i]
            print(C(0.332, 2.02, hkl))
            k2c.append(K(peak, radian=False) ** 2 * C(0.3, q, hkl))
            dk.append(dK(peak, fwhm, radian=False))
        k2c = np.array(k2c)
        dk = np.array(dk)
        plt.plot(k2c, dk, 's')
        plt.show()