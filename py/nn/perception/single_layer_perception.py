# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import time

"""
单层感知机

单层感知机只能解决线性可分问题

二分类问题：

5x - 4y > 0? 1: -1

"""


# 输入层

def model(x, y):
    if (5 * x - 4 * y - 1) > 0:
        return 1
    return -1


def random_train_data(start, stop, size, err):
    x = np.linspace(start, stop, size)
    np.random.shuffle(x)
    y = (5 * x - 1) / 4 + np.random.random(size) * err
    y = y - np.random.random(size) * err
    X = np.array([[x[i], y[i]] for i in range(x.size)])
    t = np.array([model(x[i], y[i]) for i in range(x.size)])
    return X, t


def f(x, w):
    if np.dot(x, w) + 1 > 0:
        return 1
    return -1


def update(w, input, expect, learn_rate):
    err = expect - f(input, w)
    w = w + learn_rate * err * input
    return w


def train(X, t, w, learn_rate):
    for i in range(len(X)):
        w = update(w, X[i], t[i], learn_rate)
    return w


def test(test_size, learn_rate, train_size, xlim=600):
    w = np.array([0, 0])
    X, t = random_train_data(-xlim, xlim, train_size, 300)
    w = train(X, t, w, learn_rate)
    X_test, t_test = random_train_data(-xlim, xlim, test_size, 300)
    d_test = np.array([f(x_t, w) for x_t in X_test])
    return len(d_test[d_test == t_test]) / test_size, w


if __name__ == '__main__':
    l_rates = [0.1, 0.3, 0.6, 0.9]
    test_sizes = 10000
    train_sizes = [10, 20, 50, 10000, 20000, 50000]
    for rate in l_rates:
        for train_size in train_sizes:
            t = time.time()
            acc = 0
            for i in range(5):
                accuracy, w = test(test_sizes, rate, train_size)
                print(w)
                acc = acc + accuracy
            t = (time.time() - t) / 5
            print("learn_rate:", rate, ",train_size:", train_size, ", accuracy:", acc / 5, ",use_time:", t)
