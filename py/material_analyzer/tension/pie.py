# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams['axes.titlesize'] = '12'
mpl.rcParams['font.size'] = '10'

A = [8.47, 193.77, 260.39, 407.85]
B = [8.47, 199.85, 434.16, 526.67]
labels = '$\sigma_0$', '$\sigma_{SS}$','$\sigma_{GB}$','$\sqrt{\sigma_{dis}^2 + \sigma_{p}^2}$'
plt.figure(figsize=(2, 4.5))
plt.subplot(211)
plt.pie(A, labels=labels, autopct='%1.1f%%')
plt.title('0N-A3-ODS')
plt.subplot(212)
plt.pie(B, labels=labels, autopct='%1.1f%%')
plt.title('0.5N-A3-ODS')
plt.savefig(r'C:\Users\gc_zc\Desktop\laji\writing\AB.png', dpi=1000)

