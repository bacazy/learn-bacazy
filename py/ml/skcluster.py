# -*- coding: utf-8 -*-
import imageio
from sklearn.cluster import KMeans, spectral_clustering
from skimage import color, transform, segmentation
import numpy as np
import matplotlib.pyplot as plt
import time


def readim(fname, coeff):
    img = imageio.imread(fname)
    gray_img = color.rgb2gray(img)
    gray_img = transform.rescale(gray_img, 0.4)
    m, n = gray_img.shape
    return np.array([[i, j, gray_img[i, j]] for i in range(m) for j in range(n)])


def kmeans_classify(X, fname, cl):
    labels = KMeans(cl).fit_predict(X)
    plt.figure(figsize=(6, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap=plt.get_cmap('prism'))
    plt.savefig(fname)
    plt.close()


def spectral_classify(X, fname, cls):
    labels = spectral_clustering(X, cls, eigen_solver='amg')
    plt.figure(figsize=(6, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap=plt.get_cmap('prism'))
    plt.savefig(fname)
    plt.close()


if __name__ == '__main__':
    coeffs = [600, 1500, 3125, 5000, 8000, 15000]
    clusters = [300, 500, 800, 1500]
    fn = r'C:\Users\gc_zc\Desktop\pyprj\data\A.png'
    X = imageio.imread(fn)
    segments = segmentation.slic(X, n_segments=140, compactness=2)
    plt.imshow(segments)
    plt.show()

    for cluster in clusters:
        for coeff in coeffs:
            pass
            # fname = r'C:\Users\gc_zc\Desktop\pyprj\data\A_{0}_{1}.png'.format(coeff, cluster)
            # print(fname, " starting....")
            # print(time.asctime(time.localtime(time.time())))
            # t0 = time.time()
            # spectral_classify(X, fname, cluster)
            # print("use time: ", time.time() - t0, "s")
