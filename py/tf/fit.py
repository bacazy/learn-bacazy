# -*- coding: utf-8 -*-


import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from scipy.special import gamma


def linear_model_data(start, stop, coeff, count=100, amp=2):
    """
    随机产生线性模型数据
    :return:
    """
    x = np.linspace(start, stop, count)
    y = x * coeff + amp * np.random.random_integers(-100, 100, x.size) / 100
    return x, y


def linear_fit(tf_x, tf_y, learn_rate=0.1):
    tf_coeff = tf.Variable(1.0, dtype=tf.float32)
    tf_offset = tf.Variable(1.0, dtype=tf.float32)
    tf_predict = tf.add(tf.multiply(tf_x, tf_coeff), tf_offset)
    loss = tf.reduce_sum(tf.square(tf.subtract(tf_predict, tf_y)))
    return tf.train.GradientDescentOptimizer(learning_rate=learn_rate).minimize(loss=loss)


if __name__ == '__main__':
    x, y = linear_model_data(10, 40, 2, 1000, 2)
    plt.scatter(x, y)
    X = tf.constant(x, dtype=tf.float32)
    Y = tf.constant(y, dtype=tf.float32)
    with tf.Session() as session:
        nini = tf.global_variables_initializer()
        session.run(nini)
        for i in range(101):
            result = session.run(linear_fit(X, Y))
            print(result)
