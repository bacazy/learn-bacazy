# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def k(theta, lam):
    """
    2*sin(t)/lambda
    :param theta:
    :param lam:
    :return:
    """
    return 2 * np.sin(theta) / lam


def dk(theta, fwhm, lam):
    return 2 * np.cos(theta) * fwhm / lam


def k2c(k, c):
    return k ** 2 * c


def h2(h, k, l):
    return (h ** 2 * k ** 2 + h ** 2 * l ** 2 + k ** 2 * l ** 2) / (h ** 2 + k ** 2 + l ** 2)


def hkl(hkl):
    h = int(hkl / 100)
    k = int(hkl / 10) % 10
    l = hkl % 10
    return h, k, l


if __name__ == '__main__':
    objectk = 89 * 65
