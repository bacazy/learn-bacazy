import numpy as np

import chart
import matplotlib.pyplot as plt

pipe_str = "add(3,'4')"
target_name = 'x'
pipe_str = pipe_str.strip()
bra_index = pipe_str.index('(')
method_name = pipe_str[0:bra_index].strip()
ket_index = pipe_str.rindex(')')
args = pipe_str[bra_index+1:ket_index]
ex = str(method_name + '(' + target_name + ',' + args + ')')

p_str = 'hjhdsfh '
print(p_str.split('|'))

e_str = 'a=90'


cs = chart.Generator()
fp = 'E:/laji/expriment/raw/XRD/20170527/XRD20170527.json'
cs.load(fp)
cs.draw()
