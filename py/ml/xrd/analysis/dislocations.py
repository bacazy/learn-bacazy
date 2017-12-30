# -*- coding: utf-8 -*-
import numpy as np


def h2(hkl):
    h = (np.ceil(hkl / 100)) ** 2
    k = (np.ceil(hkl / 10) % 10) ** 2
    l = (hkl % 10) ** 2
    return (h * k + k * l + h * l) / (h + k + l) ** 2


def C(C0, q, hkl):
    return C0 * (1 - q * h2(hkl))


def K(th, lam=0.54056, radian=True):
    if not radian:
        th = np.deg2rad(th)
    return 2 * np.sin(th / 2) / lam


def dK(th, fw, lam=0.54056, radian=True):
    if not radian:
        th = np.deg2rad(th)
    fw = np.deg2rad(fw)
    return 2 * np.cos(th / 2) * fw / lam
