import os
import matplotlib.image as mpimg
from google.cloud import storage
import tensorflow as tf
import tensorflow.contrib.slim as slim
from tensorflow.contrib.slim.nets import inception
from .ServiceHelper import prepare_image
from .containers.serviceContainer import Container
c = Container()


def google_download_model():
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(c.model_bucket)
    bucket = storage_client.get_bucket(c.model_bucket)
    for blob in blobs:
        blob = bucket.blob(blob.name)
        blob.download_to_filename(c.model_dir + blob.name)


def google_model_make_prediction(filename):
    tf.reset_default_graph()
    X = tf.placeholder(tf.float32, shape=[None, 299, 299, 3], name="X")
    with slim.arg_scope(inception.inception_v3_arg_scope()):
        logits, end_points = inception.inception_v3(X, num_classes=1001, is_training=False)
    with tf.name_scope("ouput"):
        flower_logits = tf.layers.dense(tf.squeeze(end_points["PreLogits"], axis=[1, 2]), 5, name="flower_logits")
        Y_proba = tf.nn.softmax(flower_logits, name="Y_proba")
    saver = tf.train.Saver()
    init = tf.global_variables_initializer()
    X_input = prepare_image(mpimg.imread(os.path.join('{0}{1}'.format(c.image_dir, filename))), 299, 299, .01)
    X_input.shape

    with tf.Session() as sess:
        init.run()
        saver.restore(sess, c.model_dir + c.model_name)
        probs = sess.run(Y_proba, feed_dict={X: X_input.reshape(-1,299,299,3)})
        return [round(f * 100, 2) for f in probs[0]]
