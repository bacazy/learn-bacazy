# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib as mpl

mpl.rcParams['lines.markersize'] = 1

dis = [16.661e14,  # 0N-ODS-R
       1.995e14,  # 0N-ODS-A3
       17.289e14,  # 0.5N-ODS-R
       3.497e14]  # 0.5N-ODS-A3

lam = 0.154056e-9
b = 0.248e-9

peaks = [44.98, 64.876, 82.343]
peaks = [i * np.pi / 180.0 for i in peaks]
x = [2 * np.sin(p) / lam for p in peaks]
y = [np.cos(p) / lam for p in peaks]

def e(dis):
    return np.sqrt(dis * np.square(b) / 14.4)


def y(x, e, D):
    return 0.9 / D - x * e

for d in dis:
    print(e(d))


fwhms = [0.533, 0.851, 0.886]
fwhms = [i * np.pi / 180 for i in fwhms]

count=2000

angle = [random.random() * 2 * np.pi for i in range(count)]
v = [random.random() for i in range(count)]


plt.polar(angle, v, 'b.')
plt.xticks([])
plt.yticks([])
plt.ylim([0,1])
plt.savefig('p.png')

