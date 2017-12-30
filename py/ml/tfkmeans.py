# -*- coding: utf-8 -*-
import time

import imageio
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from skimage import color, transform

t0 = time.time()

color_coeff = 5000
img = imageio.imread(r"D:\laji\expriment\raw\FSEM1\suojinping\zc\0T\GrainMap.png")
gray_image = color.rgb2grey(img)
gray_image = transform.rescale(gray_image, 0.2)
m, n = gray_image.shape
ps = np.array([[i, j, gray_image[i, j] * color_coeff] for i in range(m) for j in range(n)])

vectors = tf.constant(ps)

k = 100
centers = tf.Variable(tf.slice(tf.random_shuffle(vectors), [0, 0], [k, -1]))

expand_vector = tf.expand_dims(vectors, 0)
expand_center = tf.expand_dims(centers, 1)
reduce_sum = tf.reduce_sum(tf.square(tf.subtract(expand_vector, expand_center)), 2)
assignments = tf.argmin(reduce_sum, 0)

means = tf.concat(
    [tf.reduce_mean(tf.gather(vectors, tf.reshape(tf.where(tf.equal(assignments, c)), [1, -1])), reduction_indices=[1])
     for c in range(k)], 0)

update_centroides = tf.assign(centers, means)

init_op = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init_op)
# summary_writer = tf.summary.FileWriter(r"C:\logs")
# summary_writer.add_graph(sess.graph)
last = centers
diffs = []
for step in range(1001):
    pcentroides = sess.run(update_centroides)
    msg = sess.run(centers)
    if step == 1000:
        plt.figure(figsize=(12, 12))
        plt.imshow(img)
        plt.plot(msg[:, 0] * 5, msg[:, 1] * 5, 'r+')
        plt.savefig("C:/logs/image{0}.png".format(color_coeff))
print("total used: ", time.time() - t0, "s")
