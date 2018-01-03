# -*- coding: utf-8 -*-

import numpy as np


def hw_dislocations(theta, fwhm, lam, grain_size, b):
    """
    \frac{\beta cos \theta}{\lambda} = \frac{0.9}{D} + 2\eps \frac{sin \theta}{\lambda}
    \rho = 14.4 \frac{\eps^2}{b^2}
    :param theta: the diffraction angle
    :param fwhm: full width at half maximum
    :param lam: the wavelength of X-ray
    :param grain_size: grain size
    :param b: Burger vector
    :return: the density of dislocations
    """
    blob = fwhm * np.cos(theta) / lam - 0.9 / grain_size
    e = blob / (2 * np.sin(theta) / lam)
    ro = 14.4 * np.square(e) / b / b
    return ro


def peak_fit(theta, intensity, model='Vigot'):
    """

    :param theta:
    :param intensity:
    :param model:
    :return:
    """

    pass