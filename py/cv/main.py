# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy import optimize

mpl.rcParams['axes.labelsize'] = '18'
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.size'] = '14'

# 解决负号'-'显示为方块的问题
mpl.rcParams['axes.unicode_minus'] = False
# print(mpl.rcParamsDefault)
#
# data = [0.469, 0.984, 0.278]
# plt.figure(figsize=(5, 3.5))
# plt.bar([1,2,3], data, color='#00AFFF')
# plt.xticks([1,2,3], ['matrix', 'as-milled', '$H_2$ reduced'])
# plt.ylabel('FWHM(deg)')
# plt.show()

strain = "3.406,4.056,5.707,5.681,5.122,4.394,4.537,6.097,5.434,4.264,4.706,5.798," \
         "4.693,5.044,6.344,7.28,5.655,4.901,7.332,6.526"
stress = '506.25,553.91,697.92,904.07,537.98,729.69,763.19,1059.96,585.62,887.5,944.53,1215.67,888.08,977.85,1054.86,' \
         '1387.02,1004.69,970.31,1081.25,1362.61'

x = np.array([float(el) for el in strain.split(',')])
y = np.array([float(el) for el in stress.split(',')])

strain = np.array([float(el) for el in strain.split(',')])
stress = np.array([float(el) for el in stress.split(',')])
strain = strain.reshape((5, 4))
stress = stress.reshape((5, 4))

m, n = stress.shape

labels = ['R', 'A1', 'A2', 'A3', 'A4']
markers = ['o', '^', 'x', 's', 'D']
for i in range(m):
    plt.plot(strain[i, :], stress[i, :], markers[i], label=labels[i])


def strain_stress_leaner_model(x, a, b):
    return a * x + b


fa, fb = optimize.curve_fit(strain_stress_leaner_model, x, y, [1, 1])

x = np.linspace(3, 8)
y = x * fa[0] + fa[1]
plt.plot(x, y, 'r-', label='fit')

plt.xlabel('断裂延伸率(%)')
plt.ylabel('断裂强度(%)')
plt.legend()
plt.savefig(r'C:\Users\gc_zc\Desktop\laji\writing\thesis\res\ch02\fig8.png', dpi=1000)
