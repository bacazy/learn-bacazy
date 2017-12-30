# -*- coding: utf-8 -*-

import numpy as np
import scipy.misc as misc
from matplotlib import pyplot as plt
from skimage import color

gmap = r'D:\laji\expriment\raw\FSEM1\suojinping\zc\0T\GrainMap.png'
gsmap = r'D:\laji\expriment\raw\FSEM1\suojinping\zc\0T\gen.png'

img = misc.imread(gmap)

if __name__ == '__main__':
    plt.subplot(121)
    plt.imshow(img)
    plt.xlabel('raw')
    fg_img = color.rgb2grey(img)
    n, m = fg_img.shape
    entropy = []
    for i in range(2, m - 2):
        for j in range(2, n - 2):
            da = np.var(fg_img[i - 1:i + 1, j - 1:j + 1])
            if da > 0.2:
                fg_img[i - 1:i + 1, j - 1:j + 1] = fg_img[i, j]
            entropy.append(da)
    plt.subplot(122)
    plt.imshow()
    # plt.subplot(223)
    # plt.hist(entropy, bins=1000)
    plt.show()
