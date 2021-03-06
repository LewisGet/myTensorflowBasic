# taring

import numpy as np
import PIL.Image as Image
import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x,W) + b)
y_ = tf.placeholder("float", [None,10])

cross_entropy = -tf.reduce_sum(y_*tf.log(y))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

for i in range(10000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    if i % 50 == 0:
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        print (sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))


# test my png

# display int
def arrayToInt(arr):
    bigValue = 0
    returnIndex = 0

    for i, value in enumerate(arr):
        if (value > bigValue):
            bigValue = value
            returnIndex = i

    return returnIndex

# get my test photo to array
def getImageArray(fileName):
    img = Image.open(fileName).convert('1')
    arr = np.array(img)

    returnImage = []

    # format
    for x in arr:
        for y in x:
            if (y):
                returnImage.append(0.)
            else:
                returnImage.append(1.)

    return returnImage

def myTest():
    for i in range(1, 6):
        image = getImageArray("./test/" + str(i) + ".jpg")
        think = sess.run(y, feed_dict={x: [image]})
        ans = arrayToInt(think[0])

        print ("圖片 " + str(i) + ".jpg 是：" + str(ans))

    for i in range(1, 6):
        image = getImageArray("./test-full/" + str(i) + ".jpg")
        think = sess.run(y, feed_dict={x: [image]})
        ans = arrayToInt(think[0])

        print ("圖片 Full " + str(i) + ".jpg 是：" + str(ans))

myTest()