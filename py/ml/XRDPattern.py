# -*- coding: utf-8 -*-
import re
from matplotlib import pyplot as plt


class XRDPattern:
    """
    XRD pattern draw class
    """

    def __init__(self, name, filename):
        self.name = name
        self.peaks = []
        self.theta = []
        self.I = []
        self.__load(filename)

    def __load(self, filename):
        xrdfile = open(filename)
        lines = xrdfile.readlines()[32:-1]
        for xy in lines:
            x = re.findall(r'\d+\.\d+|\d+', xy)
            self.theta.append(float(x[0]))
            self.I.append(int(x[1]))

    def filter(self, method):
        pass

    def plotPeaks(self):
        plt.plot(self.theta, self.I)


if __name__ == '__main__':
    pattern = XRDPattern('xts','E:/laji/expriment/raw/XRD/20170527/2017052701/1.txt')
    pattern.plotPeaks()
    plt.show()
