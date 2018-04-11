# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np


class TfBpNet:
    def __init__(self, layers):
        self._layer_count = layers
        self._weight = []
        self._desire = tf.placeholder(name='weight', dtype=tf.float32)
        self._input = tf.placeholder(dtype=tf.float32, name='input')
        for i in range(1, len(self._layer_count)):
            self._weight.append(
                tf.Variable(tf.random_normal((self._layer_count[i - 1], self._layer_count[i]), mean=0.01), dtype=tf.float32))

    def train(self, train_data, desire, learn_rate=0.1, epochs=100):
        model = tf.train.GradientDescentOptimizer(learning_rate=learn_rate).minimize(loss=self.bp_error())
        with tf.Session() as session:
            init = tf.global_variables_initializer()
            session.run(init)
            for step in range(epochs):
                session.run(model, feed_dict={self._input: train_data, self._desire: desire})
                print(session.run(self.bp_error(), feed_dict={self._input: train_data, self._desire: desire}))

    def bp_error(self):
        output = self._input
        for w in self._weight:
            output = tf.div(1.0, 1.0 + tf.exp(- tf.matmul(output, w)))
        return tf.reduce_mean(tf.square(output - self._desire))

    def weight(self, sess):
        return sess.run(self._weight)


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
    nn = TfBpNet([2, 7, 7, 2])
    td, ds = random_train_data(10000000)
    nn.train(td, ds,epochs=10000,learn_rate=0.5)