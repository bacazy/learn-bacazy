# -*- coding: utf-8 -*-


import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


def read_xrd(fname, xmin=10.0, xmax=50.0):
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


_X, _Y = read_xrd(r'C:\Users\gc_zc\Desktop\laji\expriment\raw\XRD\20170527\2017052701\2017052701.txt'
                  , xmin=28.5, xmax=30.0)
# plt.plot(_X, _Y)
# plt.show()

N = len(_X)

X = tf.constant(_X, dtype=tf.float32)
Y = tf.constant(_Y, dtype=tf.float32)

v_A = tf.Variable(30000, dtype=tf.float32)
v_y0 = tf.Variable(9000, dtype=tf.float32)
v_wg = tf.Variable(0.3, dtype=tf.float32)
v_wl = tf.Variable(0.2, dtype=tf.float32)
v_mu = tf.Variable(0.5, dtype=tf.float32)
v_xc = tf.Variable(29.3, dtype=tf.float32)

summary_A = tf.summary.scalar('A', v_A)
summary_y0 = tf.summary.scalar('y0', v_y0)
summary_wg = tf.summary.scalar('Wg', v_wg)
summary_wl = tf.summary.scalar('Wl', v_wl)
summary_mu = tf.summary.scalar('Mu', v_mu)
summary_xc = tf.summary.scalar('Xc', v_xc)


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

opt = tf.train.AdamOptimizer(learning_rate=0.1)
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
            _ = session.run(train)
            if i % 1000 == 0:
                writer.add_summary(session.run(summary_A), i)
                writer.add_summary(session.run(summary_y0), i)
                writer.add_summary(session.run(summary_wg), i)
                writer.add_summary(session.run(summary_wl), i)
                writer.add_summary(session.run(summary_xc), i)
                writer.add_summary(session.run(summary_mu), i)
                writer.add_summary(session.run(_loss), i)
            if i % 100000 == 0:
                pd = session.run(y_predict)
                plt.plot(_X, _Y, 'b+', _X, pd, 'r-')
                # plt.show()
                plt.savefig('c:/logs/fit_' + str(i) + '.png')
                plt.close()
        writer.flush()
        writer.close()
