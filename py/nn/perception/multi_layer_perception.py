# -*- coding: utf-8 -*-
"""
# 多层感知机MLP

在单层感知机的输入层与输出层之间引入隐层，可以解决单层感知机克服线性不可分的局限性

多层前馈网络的训练常使用误差反向传播算法，因此多层前馈型网络也成为BP网络


"""

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


def bp_predict(xs, ds, ys=[10], learn_rate=0.1, epochs=3, err_threshold=0.001):
    """
    BP 网络模型预测
    :param xs: 输入
    :param ds: 期望输出
    :param ys: 隐层神经元个数，长度为隐层层数
    :param learn_rate: 学习速率
    :param epochs: 训练次数
    :return:
    """
    if not (isinstance(xs, np.ndarray) and isinstance(ds, np.ndarray) and isinstance(ys, list)):
        raise Exception('xs : np.ndarray, ds: np.ndarray, ys: list')
    input_dim = dim(xs)
    output_dim = dim(ds)
    layers = []
    layers.append(input_dim)
    for y in ys:
        layers.append(y)
    layers.append(output_dim)
    weights = []


    for i in range(1, len(layers)):
        weights.append(np.zeros((layers[i-1], layers[i])))
    E = 0
    times = 0
    while E < err_threshold and times < epochs:
        E = 0
        for x in xs:
            outs = []
            outs.append(x)
            out = sigmod(np.dot(np.transpose(weights[0]), x))
            outs.append(out)
            for i in range(1, len(weights)):
                out = sigmod(np.dot(np.transpose(weights[i]), out))
                outs.append(out)
            E = E + np.sum(np.square(out - ds))
            d_o = (ds - out) * (1 - out) * out
            prev_out = outs[-2]
            weights[-1] = weights[-1] + learn_rate * np.dot(d_o, prev_out)

            for j in range(1, len(weights)):
                sum = 0
                w_index = len(weights) - j



        E = np.sqrt(E / len(xs))
        times = times + 1

    def nn(input):

        return input

    return nn


def random_train_data(size=1000):
    x=np.random.random(size=size)
    y=np.random.random(size=size)
    return np.column_stack((x,y)), np.square(x) + np.square(y) * 0.8

if __name__ == '__main__':
    xs,ds = random_train_data(10)
    f = bp_predict(xs,ds)
    print(ds)
    print(ds[-1])

