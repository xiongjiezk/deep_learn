#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# Copyright (c) 2017 - xiongjiezk <xiongjiezk@163.com>

import tensorflow as tf
import numpy as np

# m1 = tf.constant([[1., 2.]])
# m2 = tf.constant([[1.], [2.]])
# product = tf.matmul(m1, m2)

# sess = tf.Session()
# result = sess.run(product)
# print result
# sess.close()


#使用with 代码块实现sess的关闭
# with tf.Session() as sess:
#     result = sess.run(product)
#     print result

#使用GPU计算
# with tf.Session() as sess:
#     with tf.device("/gpu:1"):
#         m1 = tf.constant([[1., 2.]])
#         m2 = tf.constant([[1.], [2.]])
#         product = tf.matmul(m1, m2)
#         result = sess.run(product)
#         print result


#使用变量 Variable 保存中间状态
# state = tf.Variable(0, name="counter")
# one = tf.constant(1)
# new_value = tf.add(state, one)
# update = tf.assign(state, new_value)  #调用run时，才会真正调用赋值操作
#
# init = tf.initialize_all_variables()
#
# with tf.Session() as sess:
#     sess.run(init)
#     print sess.run(state)
#     for _ in range(3):
#         sess.run(update)
#         print sess.run(state)  #取回结果, 也可批量取回，数组形式 sess.run([state, update])， 这个过程称之为 fetch


#feed机制
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)

with tf.Session() as sess:
  print sess.run([output], feed_dict={input1:[7.], input2:[2.]})



