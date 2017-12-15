# -*- coding: utf-8 -*-
import chart
import matplotlib.pyplot as plt
import os


cs = chart.Generator()
fp = r'E:\laji\expriment\raw\XRD\analysis\xrd.json'
cs.load(fp)
cs.draw()
