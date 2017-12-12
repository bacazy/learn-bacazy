
import chart


cs = chart.Generator()
mi = True
if mi:
    fp = 'c:/workspace/laji/expriment/raw/XRD/20170527/XRD20170527.json'
else:
    fp = 'E:/laji/expriment/raw/XRD/20170527/XRD20170527.json'
cs.load(fp)
cs.draw()
