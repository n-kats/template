import tensorflow as tf
import numpy as np

# write your model






saver = tf.train.Saver()
save_file = "save/{{_name_}}.ckpt"

with tf.Session() as sess:
	sess.run(tf.initialize_all_variables())
	# run train
	saver.save(sess, save_file)

