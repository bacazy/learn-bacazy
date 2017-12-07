# -*- coding: utf-8 -*-
import re

from matplotlib import pyplot as plt
from scipy.signal import bsplines, cubic


class XRDPattern:
    """
    XRD pattern draw class
    """

    def __init__(self):
        self.label = ''
        self.peaks = []
        self.theta = []
        self.I = []

    def load(self, filename):
        xrdfile = open(filename)
        lines = xrdfile.readlines()[32:-1]
        self.__readData(lines)

    def __readData(self, lines):
        for xy in lines:
            x = re.findall(r'\d+\.\d+|\d+', xy)
            self.theta.append(float(x[0]))
            self.I.append(int(x[1]))

    def filter(self, method):
        pass

    def plot(self):
        plt.plot(self.theta, self.I)
        plt.show()


if __name__ == '__main__':
    pattern = XRDPattern()
    pattern.load('C:/workspace/laji/expriment/raw/XRD/20170527/2017052701/1.txt')
    pattern.plot()
