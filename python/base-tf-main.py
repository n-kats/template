import tensorflow as tf
import numpy as np
# write your model
def inference():
	pass

def loss():
	pass

def training():
	pass


saver = tf.train.Saver()
save_file = "save/{{_name_}}.ckpt"

with tf.Session() as sess:
	sess.run(tf.initialize_all_variables())
	summary_writer = tf.train.SummaryWriter("summary/{{_name_}}", sess.graph)
	# run train
	saver.save(sess, save_file)

