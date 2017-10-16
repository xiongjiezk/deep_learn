#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# Copyright (c) 2017 - xiongjiezk <xiongjiezk@163.com>

import numpy as np
import tensorflow as tf

#训练数据, 随机生成
x_data = np.float32(np.random.rand(2, 100))
y_data = np.dot([0.100, 0.200], x_data) + 0.300    # y = w0*x0 + w1*x1 + b

#构造训练模型
b = tf.Variable(tf.zeros([1]))
W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
y = tf.matmul(W, x_data) + b

loss = tf.reduce_mean(tf.square(y - y_data))  # reduce_mean 针对指定的维度求和
optimazier = tf.train.GradientDescentOptimizer(0.5)
train = optimazier.minimize(loss)

init = tf.initialize_all_variables()

sess = tf.Session()

sess.run(init)

for step in xrange(0, 200):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))


