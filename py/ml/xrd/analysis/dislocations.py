# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize


def HSquare(hkl):
    h = int(hkl / 100) % 10
    k = int(hkl / 10) % 10
    l = hkl % 10
    h2 = h ** 2
    k2 = k ** 2
    l2 = l ** 2
    return (h2 * k2 + k2 * l2 + h2 * l2) / (h2 + k2 + l2) ** 2


def K(lam, theta):
    theta = theta * np.pi / 180
    return 2 * np.sin(theta) / lam


def toArc(t):
    return t * np.pi / 180.0


def DeltaK(lam, theta, fwhm):
    return 2 * np.cos(theta) * fwhm / lam


def C(c0, q, hkl):
    r = c0 * (1 - q * HSquare(hkl))
    return r


def k2c(k, c):
    return k ** 2 * c


def dislocation_density(peaks, fws, hkls, lam=0.154, c0=0.266, q=2):
    def linear_model(x, a, b):
        return a * x + b

    k2cs = []
    dks = []
    for i in range(len(peaks)):
        p = peaks[i]
        fw = fws[i]
        hkl = hkls[i]
        dks.append(DeltaK(lam, p, fw))
        k2cs.append(k2c(K(lam, p), C(c0, q, hkl)))

    print(dks)
    params, params_c = optimize.curve_fit(linear_model, k2cs, dks)
    print(params[0])
    plt.xlabel('$K^2C$')
    plt.ylabel('$\Delta K$')
    plt.plot(k2cs, dks, 's')
    x = np.arange(0, np.max(k2cs) + 0.2, 0.1)
    y = x * params[0] + params[1]
    plt.plot(x, y)
    plt.show()


def hw_dislocations(theta, fwhm, lam, size, b):
    """
    \frac{\beta cos \theta}{\lambda} = \frac{0.9}{D} + 2\eps \frac{sin \theta}{\lambda}
    \rho = 14.4 \frac{\eps^2}{b^2}
    :param theta: the diffraction angle
    :param fwhm: full width at half maximum
    :param lam: the wavelength of X-ray
    :param size: grain size
    :param b: Burger vector
    :return: the density of dislocations
    """
    blob = fwhm * np.cos(theta) / lam - 0.9 / size
    e = blob / (2 * np.sin(theta) / lam)
    ro = 14.4 * np.square(e) / b / b
    return ro


if __name__ == '__main__':
    peaks = [44.447, 64.543, 81.912]
    peaks = [i * np.pi / 180.0 for i in peaks]
    fws = [0.566, 0.861, 0.840]
    hkls = [110, 200, 211]
    r = hw_dislocations(np.deg2rad(peaks[0]), 0.566, 0.154, 1.3, 0.3)
    print(r)

