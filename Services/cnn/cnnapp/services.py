import os
import numpy as np
import tensorflow as tf
import matplotlib.image as mpimg
import tensorflow.contrib.slim as slim
from skimage.transform import resize
from tensorflow.contrib.slim.nets import inception

def prepare_image(image, target_width, target_height, max_zoom):
    height = image.shape[0]
    width = image.shape[1]
    image_ratio = width / height
    target_image_ratio = target_width / target_height
    crop_vertically = image_ratio < target_image_ratio
    
    crop_width = width if crop_vertically else int(height * target_image_ratio)
    crop_height = int(width / target_image_ratio) if crop_vertically else height
    
    resize_factor = np.random.rand() * max_zoom + 1.0
    crop_width = int(crop_width / resize_factor)
    crop_height = int(crop_height / resize_factor)
    
    x0 = np.random.randint(0, width - crop_width)
    y0 = np.random.randint(0, height - crop_height)
    x1 = x0 + crop_width
    y1 = y0 + crop_height

    return resize(image[y0:y1, x0:x1], (target_width, target_height)).astype(np.float32)


def make_prediction(filename):
	tf.reset_default_graph()
	
	X = tf.placeholder(tf.float32, shape=[None, 299, 299, 3], name="X")
	
	with slim.arg_scope(inception.inception_v3_arg_scope()):
		logits, end_points = inception.inception_v3(X, num_classes=1001, is_training=False)
		
	with tf.name_scope("ouput"):
		flower_logits = tf.layers.dense(tf.squeeze(end_points["PreLogits"], axis=[1, 2]), 5, name="flower_logits")
		Y_proba = tf.nn.softmax(flower_logits, name="Y_proba")
	
	saver = tf.train.Saver()
	init = tf.global_variables_initializer()
	
	X_input = prepare_image(mpimg.imread(os.path.join('./cnnapp/images/{0}'.format(filename))), 299, 299, .01)
	X_input.shape
	
	with tf.Session() as sess:
		init.run()
		saver.restore(sess, './cnnapp/model/flower_classifier.ckpt')
		probs = sess.run(Y_proba, feed_dict={X: X_input.reshape(-1,299,299,3)})
		return [round(f * 100, 2) for f in probs[0]]
