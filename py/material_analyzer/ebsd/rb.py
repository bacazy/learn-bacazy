# -*- coding: utf-8 -*-
from numba import cuda
import time
import numpy as np
import imageio
from matplotlib import pyplot as plt
from skimage import segmentation
import matplotlib as mpl
from random import shuffle

img_dir = r'C:\Users\gc_zc\Desktop\pyprj\data\image_'
gmap = r'C:\Users\gc_zc\Desktop\pyprj\data\8b.png'

img = imageio.imread(gmap)

cmaps = [
    'viridis', 'plasma', 'inferno', 'magma',
    'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
    'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
    'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn',
    'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
    'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
    'hot', 'afmhot', 'gist_heat', 'copper',
    'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
    'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic',
    'Pastel1', 'Pastel2', 'Paired', 'Accent',
    'Dark2', 'Set1', 'Set2', 'Set3',
    'tab10', 'tab20', 'tab20b', 'tab20c',
    'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
    'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
    'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']


def segment(rimg, n, compact, iters):
    image = segmentation.slic(rimg, n_segments=n, compactness=compact, max_iter=iters)
    return image


def get_name(name):
    return img_dir + name + ".png"


def convert(array):
    array = np.array(array)
    m, n = array.shape
    csets = set([])
    for i in range(m):
        for j in range(n):
            csets.add(array[i, j])
    clist = [i for i in csets]
    ctos = [i for i in csets]
    print(ctos)
    shuffle(ctos)
    print(ctos)
    print('---------------------')
    cmap = {}
    for i in range(len(ctos)):
        cmap[clist[i]] = ctos[i]
    for i in range(m):
        for j in range(n):
            d = array[i, j]
            array[i, j] = cmap[d]
    return array


if __name__ == '__main__':
    t0 = time.time()
    for i in [0.000001, 0.001, 0.01, 0.1]:
        asim = convert(segment(img, 100, i, 50))
        for map in ['brg']:
            plt.figure(figsize=(8, 8))
            plt.imshow(asim, cmap=plt.get_cmap(map))
            plt.savefig(get_name(str(i) + "_" + map), dpi=600)
            plt.close()
    print('use ', time.time() - t0, 's')
