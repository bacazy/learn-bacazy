# -*- coding: utf-8 -*-

import tensorflow as tf


def load_tension_data(tension_file, format='tra'):
    pass


def tension_analysis(X, Y, gauge, width, thickness):
    with tf.Graph().as_default() as gf:
        x = tf.constant(X)
        y = tf.constant(Y)
