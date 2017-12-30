# -*- coding: utf-8 -*-
import time

import imageio
import matplotlib.pyplot as plt
from skimage import color

t0 = time.time()

color_coeff = 500
clusters = 80
img = imageio.imread(r"C:\Users\gc_zc\Desktop\pynote\data\small.png")
gray_image = color.rgb2grey(img)
# gray_image = transform.rescale(gray_image, 0.5)
# m, n = gray_image.shape
# print(m,n)
# ps = np.array([[i, j, gray_image[i, j] * color_coeff] for i in range(m) for j in range(n)])
#
# labels = KMeans(n_clusters=clusters).fit_predict(ps)
#
# print(labels)
cmaps = [('Perceptually Uniform Sequential', [
    'viridis', 'plasma', 'inferno', 'magma']),
         ('Sequential', [
             'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
             'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
             'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']),
         ('Sequential (2)', [
             'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
             'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
             'hot', 'afmhot', 'gist_heat', 'copper']),
         ('Diverging', [
             'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
             'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']),
         ('Qualitative', [
             'Pastel1', 'Pastel2', 'Paired', 'Accent',
             'Dark2', 'Set1', 'Set2', 'Set3',
             'tab10', 'tab20', 'tab20b', 'tab20c']),
         ('Miscellaneous', [
             'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
             'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
             'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar'])]
for c in cmaps:
    for name in c[1]:
        print(name)
        plt.figure(figsize=(5, 5))
        # plt.scatter(ps[:, 0], ps[:, 1], c=labels, cmap=plt.get_cmap('spring'))
        plt.imshow(gray_image, cmap=plt.get_cmap(name))
        plt.xlabel(name)
        plt.savefig("c:/logs/image_{0}.png".format(name))
        plt.close()
