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
                tf.Variable(tf.random_normal((self._layer_count[i - 1], self._layer_count[i]), mean=0.01),
                            dtype=tf.float32))

    def train(self, train_data, desire, learn_rate=0.1, epochs=100):
        loss = self.bp_error()
        saver = tf.train.Saver()
        summary_loss = tf.summary.scalar('err', loss)
        model = tf.train.GradientDescentOptimizer(learning_rate=learn_rate).minimize(loss=loss)
        with tf.Session() as session:
            writer = tf.summary.FileWriter('c:/logs', session.graph)
            try:
                saver.restore(session, './model/model.cpt')
            except:
                session.run(tf.global_variables_initializer())
            for step in range(epochs):
                s_loss, _ = session.run([summary_loss, model],
                                        feed_dict={self._input: train_data, self._desire: desire})
                if step % 1000 == 0:
                    writer.add_summary(s_loss, step)
                    saver.save(session, './model/model.cpt')
                    print(step)

    def output(self, input):
        output = input
        for w in self._weight:
            output = tf.div(1.0, 1.0 + tf.exp(- tf.matmul(output, w)))
        return output

    def bp_error(self):
        return tf.reduce_mean(tf.square(self.output(self._input) - self._desire))

    def weight(self, sess):
        return sess.run(self._weight)

    def predict(self, input):
        tf_in = tf.constant(input, dtype=tf.float32)
        out = self.output(tf_in)
        saver = tf.train.Saver()
        with tf.Session() as sess:
            saver.restore(sess, './model/model.cpt')
            return sess.run(out)


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


def test():
    nn = TfBpNet([2, 7, 7, 2])
    for i in range(100):
        td, ds = random_train_data(1)
        # nn.train(td, ds,epochs=1000,learn_rate=0.1)
        print(td, ds, nn.predict(td))


if __name__ == '__main__':
    nn = TfBpNet([2, 7, 14, 7, 2])
    td, ds = random_train_data(10000)
    # nn.train(td, ds, epochs=100001, learn_rate=0.8)
    for i in range(10):
        td, ds = random_train_data(1)
        # nn.train(td, ds,epochs=1000,learn_rate=0.1)
        print(td, ds, nn.predict(td))
