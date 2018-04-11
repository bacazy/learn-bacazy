# -*- coding: utf-8 -*-


import numpy as np


def dim(x):
    if isinstance(x, np.ndarray):
        if len(x.shape) == 2:
            return x.shape[1]
        else:
            return 1
    else:
        raise Exception('x must be ndarray')


def sigmod(x):
    return 1 / (1 + np.exp(-x))


def tri_layer_bp(xs, ds, ycount=10, learn_rate=0.1, epochs=3, err_threhold=0.01):
    W = np.zeros((ycount, dim(ds)))
    V = np.zeros((dim(xs), ycount))
    q = 0
    E = 0
    while (q < epochs and E < err_threhold):
        E = 0
        for i in range(len(xs)):
            x=xs[i]
            d=ds[i]
            y = sigmod(np.dot(np.transpose(V), x))
            o = sigmod(np.dot(np.transpose(W), y))
            E = E + np.sum(np.square(ds - o))
            del_ko = (d - o) * (1 - o) * o
            del_jy = []
            for j in range(dim(ds)):
                del_jy.append(np.sum(del_ko * W[j,:]))
            del_jy = np.array(del_jy)
            del_jy = del_jy * (1 - y) * y
            W = W + learn_rate * del_ko * y
            V = V + learn_rate * del_jy * x

        E = np.sqrt(E / len(xs))
        q = q + 1

    def f(input):
        y = sigmod(np.dot(np.transpose(V), input))
        return sigmod(np.dot(np.transpose(W), y))

    return f


def random_train_data(size=1000):
    x = np.random.random(size=size)
    y = np.random.random(size=size)
    return np.column_stack((x, y)), np.square(x) + np.square(y) * 0.8


if __name__ == '__main__':
    xs, ds = random_train_data(10)
    f = tri_layer_bp(xs, ds)
    print(ds)
    print(ds[-1])
