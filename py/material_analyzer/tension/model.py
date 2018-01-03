# -*- coding: utf-8 -*-
import numpy as np

from xrd import hw_dislocations, loadfit


class StrengthModel:
    def __init__(self):
        self.fname = ''
        self.models = []
        self.params = {}
        self.metas = {}

    def add_params(self, kws={}):
        for k, v in kws:
            self.params[k] = v

    def ready(self):
        if self.params.__contains__('dislocation_density'):
            self.refresh()
        else:
            if self.params.__contains__('xrd_fit_file'):
                self.__dislocations_density__()
            else:
                raise Exception('dislocation_density should be specified or the xrd_fit_file should be specified')

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
            solid_solution = np.sum([k * np.power(c, z) for k, c, z in zip(K, C, Z)])
            self.metas['solid_solution_stress'] = solid_solution
        return self.metas['solid_solution_stress']

    def __grain_boundary__(self, refresh=False):
        if refresh or not self.metas.__contains__('grain_boundary_stress'):
            grain_size = self.__get_float__('grain_size')
            KGB = self.__get_float__('KGB')
            grain_boundary_stress = KGB / np.sqrt(grain_size)
            self.metas['grain_boundary_stress'] = grain_boundary_stress
        return self.metas['grain_boundary_stress']

    def __dislocations_precipitates__(self, refresh=False):
        if refresh or not self.metas.__contains__('dislocations_stress') or not self.metas.__contains__(
                'precipitates_stress'):
            self.__dislocations__()
            self.__precipitates__()
        dis = self.metas['dislocations_stress']
        pars = self.metas['precipitates_stress']
        return np.sqrt(np.square(dis) + np.square(pars))

    def __dislocations__(self):
        alpha = self.__get_float__('alpha')
        density = self.__get_float__('dislocation_density')
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
        denominator = 2 * np.pi * np.sqrt(1 - v) * np.sqrt(2 * np.pi / 3 / f * r)
        self.metas['precipitates_stress'] = numerator / denominator

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
        return sum

    def __dislocations_density__(self):
        fit_file = self.get_param('xrd_fit_file')
        data = loadfit(fit_file)
        theta = data['2theta'][0] / 2.0
        fwhm = data['FWHM']
        lam = self.__get_float__('lambda')
        g_size = self.__get_float__('grain_size')
        b = self.__get_float__('b')
        theta = np.deg2rad(theta)
        fwhm = np.deg2rad(fwhm)
        self.metas['dislocation_density'] = hw_dislocations(theta=theta, fwhm=fwhm, lam=lam, grain_size=g_size, b=b)


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


if __name__ == '__main__':
    models = load_models(r'E:\laji\writing\n-ods\report.csv')
    for m in models:
        print(m.get_metas())
        print(m.predict_stress())
