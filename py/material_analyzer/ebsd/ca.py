# -*- coding: utf-8 -*-
from random import random

import tensorflow as tf

def readimg(fname):
    return tf.constant([[1, 2], [1, 2]], dtype=tf.float64)


def evolve(status, coeff):

    return status


def main(epochs=10000):
    init = tf.global_variables_initializer()
    with tf.Session() as session:
        session.run(init)
        for epoch in range(epochs):
            img = session.run(evolve(status=readimg('')))


if __name__ == '__main__':
    for i in range(15):
        print(random() - 0.5)
