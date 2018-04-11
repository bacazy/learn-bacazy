# -*- coding: utf-8 -*-

import numpy as np
import pickle
import os


class BpNetwork:
    def __init__(self, layers):
        self._layers_count = layers
        self._layers = []
        self._weight = []
        self._random_weight()

    def train(self, train_data, desire, learn_rate=0.1, epochs=1000, err_threhold=0.01, load=False,
              save_interval=1000):
        if load:
            if os.path.exists('ws'):
                with open('ws', 'rb') as f:
                    self._weight = pickle.load(f)
            else:
                print('load fail, not exits')
        epoch = 0
        err = np.inf
        e_l = 10
        while (epoch < epochs) and (err > err_threhold):
            err = 0
            for i in np.arange(0, len(train_data)):
                x = train_data[i]
                d = desire[i]
                self._layers.clear()
                self._layers.append(x)
                # 计算各层输出
                for w in self._weight:
                    self._layers.append(self._single_layer_output(w, self._layers[-1]))
                err = err + np.sum(np.square(self._output() - d))
                self._update_weight(d, learn_rate)

            err = np.sqrt(err / len(train_data))
            epoch = epoch + 1
            if epoch % save_interval == 0:
                self.save()
            print(epoch, err, (e_l - err) * 100 / e_l)
            e_l = err
        return self

    def _random_weight(self):
        c = 0
        self._weight.clear()
        for lc in self._layers_count:
            if c == 0:
                c = lc
                self._layers.append(np.zeros(c))
            else:
                w = np.random.random((c, lc))/10000
                c = lc
                self._weight.append(w)
                self._layers.append(np.zeros(lc))

    @staticmethod
    def _single_layer_output(w, input):
        if not (isinstance(w, np.ndarray) and isinstance(input, np.ndarray)):
            raise Exception('Illegal args')
        return BpNetwork._activate(np.dot(np.transpose(w), input))

    @staticmethod
    def _activate(x):
        return 1 / (1 + np.exp(-x))

    def predict(self, input):
        y = input
        for w in self._weight:
            y = self._single_layer_output(w, y)
        return y

    def _output(self):
        return self._layers[-1]

    def _update_weight(self, d, learn_rate):
        d_last = (d - self._output()) * self._output() * (1 - self._output())
        self._weight[-1] = self._weight[-1] + learn_rate * np.dot(self._layers[-2].reshape((len(self._layers[-2]), 1)),
                                                                  d_last.reshape((1, len(d_last))))
        index = len(self._weight) - 2
        while index >= 0:
            d_last = np.dot(self._weight[index + 1], d_last) * self._layers[index + 1] * (1 - self._layers[index + 1])
            self._weight[index] = self._weight[index] + learn_rate * np.dot(
                self._layers[index].reshape((len(self._layers[index]), 1)),
                d_last.reshape((1, len(d_last))))
            index = index - 1

    def save(self):
        with open('ws', 'wb') as f:
            pickle.dump(self._weight, f)


def random_train_data(size=1000):
    train_data = []
    desire = []

    for i in range(size):
        x = np.random.random()
        y = np.random.random()
        t1 = (x ** 2 + y ** 2) / 2
        t2 = (x ** 2 + x + np.exp(-y ** 2)) / 3
        train_data.append([x, y])
        desire.append([t1, t2])
    return np.array(train_data), np.array(desire)


if __name__ == '__main__':
    bpnn = BpNetwork([2, 5, 2])
    td, ds = random_train_data(1000)
    for rate in np.linspace(0.8, 0.01, 80):
        bpnn.train(td, ds, epochs=1002, learn_rate=rate, err_threhold=0.001, load=True, save_interval=1000).save()
        tds, dss = random_train_data(100)
        for i in range(len(tds)):
            print(bpnn.predict(tds[i]), dss[i])
