# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np


def main():
    ay = tf.constant(np.linspace(0, 100, 1000), dtype='array')
    sub = tf.slice(ay, 100, 100)


if __name__ == '__main__':
    main()
