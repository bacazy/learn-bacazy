# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from xrd.io import xrd_dir_map, get_xrd_file

from xrd import hw_dislocations, loadfit


class StrengthModel:
    def __init__(self):
        self.fname = ''
        self.models = []
        self.params = {}
        self.metas = {}

    def add_params(self, kws={}):
        for k in kws.keys():
            self.params[k] = kws[k]

    def ready(self):
        if not self.params.__contains__('dislocation_density'):
            if self.params.__contains__('XRD'):
                self.__dislocations_density__()
            else:
                raise Exception('dislocation_density should be specified or the XRD should be specified')
        self.refresh()

    def get_param(self, key, dtype='str'):
        if not self.params.__contains__(key):
            raise Exception(key, 'not found')
        if dtype == 'str':
            return self.params[key]
        elif dtype == 'float':
            return float(self.params[key])
        elif dtype == 'int':
            return int(self.params[key])

    def set_param(self, key, value):
        self.params[key] = value

    def get_meta_names(self):
        return self.metas.keys()

    def get_metas(self):
        return self.metas

    def get_meta(self, name):
        return self.metas[name]

    def __lattice__(self, refresh=False):
        if refresh or not self.metas.__contains__('lattice_stress'):
            v = self.__get_float__('v')
            M = self.__get_float__('M')
            u = self.__get_float__('u')
            b = self.__get_float__('b')
            a = self.__get_float__('a')
            coeff = 2 * M * u / (1 - v)
            lattice = coeff * np.exp(-2 * np.pi * a / b / (1 - v))
            self.metas['lattice_stress'] = lattice
        return self.metas['lattice_stress']

    def __get_float__(self, key):
        return self.get_param(key, dtype='float')

    def __solid__solution__(self, refresh=False):
        if refresh or not self.metas.__contains__('solid_solution_stress'):
            K = self.get_param('K')
            C = self.get_param('C')
            Z = self.get_param('Z')
            K = [float(k.strip()) for k in K.split(';')]
            C = [float(c.strip()) for c in C.split(';')]
            Z = [float(z.strip()) for z in Z.split(';')]
            solid_solution = [0.00689 * k * np.power(c, z) for k, c, z in zip(K, C, Z)]
            print(self.get_param('name'), solid_solution)
            self.metas['solid_solution_stress'] = np.sum(solid_solution) * 1e6
        return self.metas['solid_solution_stress']

    def __grain_boundary__(self, refresh=False):
        if refresh or not self.metas.__contains__('grain_boundary_stress'):
            grain_size = self.__get_float__('grain_size')
            KGB = self.__get_float__('KGB')
            grain_boundary_stress = KGB / np.sqrt(grain_size)
            self.metas['grain_boundary_stress'] = grain_boundary_stress
        return self.metas['grain_boundary_stress']

    def __dislocations_precipitates__(self, refresh=False):
        if refresh or not self.metas.__contains__('dis_particles_stress'):
            self.__dislocations__()
            self.__precipitates__()
            dis = self.metas['dislocations_stress']
            pars = self.metas['precipitates_stress']
            self.metas['dis_particles_stress'] = np.sqrt(np.square(dis) + np.square(pars))
        return self.metas['dis_particles_stress']

    def __dislocations__(self):
        alpha = self.__get_float__('alpha')
        density = self.params['dislocation_density']
        M = self.__get_float__('M')
        u = self.__get_float__('u')
        b = self.__get_float__('b')
        self.metas['dislocations_stress'] = M * alpha * u * b * np.sqrt(density)

    def __precipitates__(self):
        M = self.__get_float__('M')
        u = self.__get_float__('u')
        b = self.__get_float__('b')
        v = self.__get_float__('v')
        r = self.__get_float__('r')
        f = self.__get_float__('f')
        numerator = 0.81 * M * u * b * np.log(np.sqrt(2.0 / 3) * r / b)
        denominator = 2 * np.pi * np.sqrt(1 - v) * np.sqrt(2 * np.pi / 3 / f) * r
        precipitate = numerator / denominator
        self.metas['precipitates_stress'] = precipitate

    def refresh(self):
        self.__lattice__(refresh=True)
        self.__solid__solution__(refresh=True)
        self.__grain_boundary__(refresh=True)
        self.__dislocations_precipitates__(refresh=True)

    def predict_stress(self):
        sum = 0
        for k in self.metas.keys():
            if k.endswith('_stress'):
                sum = sum + self.metas[k]
        return sum - self.metas['dislocations_stress'] - self.metas['precipitates_stress']

    def __dislocations_density__(self):
        fname = self.get_param('xrd_report')
        target = self.get_param('XRD')
        self.params['dislocation_density'] = dis_density(fname, target)
        self.metas['dislocation_density'] = dis_density(fname, target)


def load_models(fname):
    models = []
    cnames = []
    with open(fname) as fp:
        header = fp.readline()
        cnames = header.split(',')
    cnames = [name.strip() for name in cnames]
    data = np.loadtxt(fname, dtype=str, skiprows=1, delimiter=',')
    m, n = data.shape
    for i in range(m):
        m = StrengthModel()
        for j in range(n):
            m.set_param(cnames[j], data[i, j])
        models.append(m)
    return models


def collect_data(models, key):
    data = [m.get_meta(key) for m in models]
    return np.array(data)


def stack_bar_chart(models):
    mpl.rcParams['xtick.labelsize'] = 14
    mpl.rcParams['ytick.labelsize'] = 14
    mpl.rcParams['axes.labelsize'] = 14
    mpl.rcParams['legend.fontsize'] = 12
    plt.figure(figsize=(7, 5))

    lattices = collect_data(models, 'lattice_stress') / 1e6
    grain_size = collect_data(models, 'grain_boundary_stress') / 1e6
    solid_solution = collect_data(models, 'solid_solution_stress') / 1e6
    dis_par = collect_data(models, 'dis_particles_stress') / 1e6
    size = lattices.size
    width = 0.35
    ind = [1, 2]

    plt.bar(ind, lattices, width, label='lattice')
    plt.bar(ind, solid_solution, width, label='solid solution', bottom=lattices)
    plt.bar(ind, grain_size, width, label='grain size', bottom=lattices + solid_solution)
    plt.bar(ind, dis_par, width, label='dislocations and precipitates', bottom=grain_size + lattices + solid_solution)

    plt.bar([1.3, 2.3], [888.08, 1208], width/4, label='experimental')

    labels = [m.get_param('name') for m in models]
    plt.ylim([0, 1500])
    plt.ylabel('Stress (MPa)')
    plt.xticks([1.1, 2.1], labels)
    plt.legend()
    plt.savefig('E:/figure.png', dpi=800)


def dis_density(fname, target):
    xrd = xrd_dir_map(fname)[target]
    xrd_file = get_xrd_file(xrd['dir'], 'fit')
    xrd_fit = loadfit(xrd_file, 10)
    thetas = xrd_fit['2theta'][:3]
    fwhms = xrd_fit['FWHM'][:3] - np.array([0.12, 0.02, 0.0])
    lam = 0.154056
    fwhms = np.deg2rad(fwhms)
    thetas = np.deg2rad(thetas)
    y = fwhms * np.cos(thetas) / lam
    x = 2 * np.sin(thetas) / lam
    e = (y[1]-y[0])/(x[1]- x[0])
    p = 14.4 * e * e / (np.square(2.48e-10))
    return p


if __name__ == '__main__':
    models = load_models(r'E:\laji\writing\n-ods\report.csv')
    for m in models:
        m.add_params({'xrd_report': r'E:\laji\writing\n-ods\xrd.csv'})
        m.ready()
    for m in models:
        print(m.get_metas())
        print(m.predict_stress())

    stack_bar_chart(models)
