import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
import os
mnist = input_data.read_data_sets(os.path.expanduser("~/data/MNIST_data/"), one_hot=True)

batch_size = 100 # TODO
steps = 1000 # TODO

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

# write your model








# TODO y_ = ...

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_*tf.log(y), reduction_indices=[1]))

# train = tf.train...

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
	sess.run(tf.initialize_all_variables())

	for i in range(steps):
		batch_xs, batch_ys = mnist.train.next_batch(batch_size)

		if (i+1) % 100 == 0:
			train_acc = sess.run(accuracy, {x: batch_xs, y: batch_ys})
			print("step %d, train accuracy %g" % (100, train_acc))
		sess.run(train, {x: batch_xs, y: batch_ys})

	acc = sess.run(accuracy, {x: mnist.test.images, y_: mnist.test.labels})
	print("test accuracy %g" % acc)

