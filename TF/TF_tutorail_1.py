'''This is a modified Version of Google's TensorFlow(TF) Tutorial. Here you will learn about the TF variable, placeholder and linear optimization model.

By Dr. Mohendra Roy

'''

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
sess = tf.Session()

# initial variable for weights and biases
w = tf.Variable(3.0)
b = tf.Variable(4.0)
init = tf.global_variables_initializer()  # handler to initiate the global variable
sess.run(init)
wini = sess.run(w)
bini = sess.run(b)
# initial placeholder for input data and labels

x = tf.placeholder(tf.float32)  # for input data
y = tf.placeholder(tf.float32)  # fro label

# linear model

lm = x*w + b

# Setting the desired goal

loss = tf.reduce_sum(tf.square(lm - y))
lossini = sess.run(loss, {x: [1, 2, 3], y: [0, -1, -2]})

''' Our desired goal is to reduce the difference between the training input and training label '''

''' To achieve this we will use a optimization method using the Gradient Descent Optimizer algorithm '''

# The optimizer with Gradient Descent Optimizer

op = tf.train.GradientDescentOptimizer(0.01)  # The number here is the step at which the optimization will descent
ob = op.minimize(loss)  # The objective(ob) is to minimize the loss

''' Our main objective is to reduce the loss, i.e. the difference between the training input and label '''

''' Now we will  train our model in a loop to get the minimum loss by updating weight and biases '''

# Training loop
for i in range(1000):
    sess.run(ob, {x: [1, 2, 3], y: [0, -1, -2]})


wfi = sess.run(w)  # final weight after training
bfi = sess.run(b)  # final bias after training
lossfi = sess.run(loss, {x: [1, 2, 3], y: [0, -1, -2]})

print("Initial weight: %s, Bias: %s, Loss: %s " % (wini, bini, lossini))  # The weight, bias and loss before training

print("Final weight: %s, Bias: %s, Loss: %s " % (wfi, bfi, lossfi))  # The weight, bias and loss after training

''' Till this we just train our 1st linear model. However we want to test the model too  '''


# Testing of the model
xin = 2
y = sess.run(lm, {x: xin})
print("The calculated output for input  %x is = "%xin, y)

