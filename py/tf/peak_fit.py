# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


def read_xrd(fname, xmin=10, xmax=50):
    data = np.loadtxt(fname, skiprows=2)
    theta = data[:, 0]
    intensity = data[:, 1]
    mask = theta > xmin
    theta = theta[mask]
    intensity = intensity[mask]
    mask = theta < xmax
    intensity = intensity[mask]
    theta = theta[mask]
    return theta, intensity


_X, _Y = read_xrd(r'C:\Users\gc_zc\Desktop\laji\expriment\raw\XRD\analysis\ods\powder_10_v_r.txt'
                  , xmin=43.5, xmax=46)
plt.plot(_X, _Y)
plt.show()

N = len(_X)

X = tf.constant(_X, dtype=tf.float32)
Y = tf.constant(_Y, dtype=tf.float32)

v_A = tf.Variable(10000.0, dtype=tf.float32)
v_y0 = tf.Variable(0, dtype=tf.float32)
v_wg = tf.Variable(1.0, dtype=tf.float32)
v_wl = tf.Variable(1.0, dtype=tf.float32)
v_mu = tf.Variable(0.5, dtype=tf.float32)
v_xc = tf.Variable(0, dtype=tf.float32)

t_c4 = tf.constant(4.0, dtype=tf.float32)
t_c2 = tf.constant(2.0, dtype=tf.float32)
t_c1 = tf.constant(1.0, dtype=tf.float32)
t_N = tf.constant(N-1.0, dtype=tf.float32)

t_xxc = tf.square(tf.subtract(X, v_xc))
t_wg2 = tf.square(v_wg)
t_wl2 = tf.square(v_wl)

t_div_bottom = tf.add(tf.multiply(t_c4, t_xxc), t_wl2)
t_div = tf.div(v_wl, t_div_bottom)
t_mul = tf.multiply(tf.div(t_c2, np.pi), t_div)

y_MA = tf.multiply(v_mu, t_mul)

t_b_coeff = tf.subtract(t_c1, v_mu)

t_cf1 = tf.constant(np.sqrt(4.0 * np.log(2.0) / np.pi), dtype=tf.float32)
t_cf2 = tf.constant(-4.0 * np.log(2.0), dtype=tf.float32)

t_b_divm = tf.div(t_cf1, v_wg)
t_b_coeff = tf.multiply(t_b_coeff, t_b_divm)
t_zhishu = tf.div(t_cf2, t_wg2)
t_zhishu = tf.multiply(t_zhishu, t_xxc)
y_MB = tf.multiply(t_b_coeff, tf.exp(t_zhishu))

y_M = tf.add(y_MA, y_MB)
y_predict = tf.add(v_y0, tf.multiply(v_A, y_M))
loss = tf.reduce_sum(tf.square(tf.subtract(y_predict, Y)))
nloss = tf.div(loss, t_N)
_loss = tf.summary.scalar(name='loss', tensor=nloss)

opt = tf.train.AdadeltaOptimizer(learning_rate=0.1)
train = opt.minimize(tf.cast(nloss, dtype=tf.float32))

if __name__ == '__main__':
    with tf.Session() as session:

        initial = tf.global_variables_initializer()
        session.run(initial)
        steps = 10000000
        writer = tf.summary.FileWriter('c:/logs',
                                       graph=session.graph,
                                       flush_secs=2)
        tf.summary.merge_all()
        for i in np.arange(start=0, stop=steps + 1):
            _, summary, mesu = session.run([train, _loss, nloss])
            if i % 100 == 0:
                writer.add_summary(summary, i)
            if i % 1000 == 0:
                print(mesu)
        writer.flush()
        writer.close()
