import numpy as np
import chart
import matplotlib.pyplot as plt


cs = chart.Generator()

d = np.loadtxt(fname='C:/workspace/laji/expriment/raw/XRD/20170527/2017052701/2017052701.txt',
               skiprows=1)

print(len(d.shape))


fp = 'C:/workspace/laji/expriment/raw/XRD/20170527/XRD20170527.json'
cs.load(fp)
cs.draw()




