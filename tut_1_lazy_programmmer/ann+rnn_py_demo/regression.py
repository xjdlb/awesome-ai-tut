# -*- coding: utf-8 -*-
"""regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1faOxgVoRq-GoSux1hedGd6PlfuYB3TNt
"""

import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
import tensorflow_datasets as tfds

!wget https://raw.githubusercontent.com/lazyprogrammer/machine_learning_examples/master/tf2.0/moore.csv

df = pd.read_csv('moore.csv',header=None)

data = df.values

X = data[:,0].reshape(-1,1)
Y = data[:,1]
plt.scatter(X, Y)

Y = np.log(Y)
plt.scatter(X,Y)

X = X - X.mean()

# model
model = tf.keras.models.Sequential([tf.keras.layers.Input(shape=(1,)), tf.keras.layers.Dense(1)])
model.compile(optimizer=tf.keras.optimizers.SGD(0.001, 0.9), loss=tf.keras.losses.MSE)

# learning rate scheduler
def schedule(epoch, lr):
    if epoch >= 50:
        return 0.0001
    else:
        return 0.001

scheduler = tf.keras.callbacks.LearningRateScheduler(schedule)
r = model.fit(X, Y, epochs=200, callbacks=[scheduler])

plt.plot(r.history['loss'],label='loss')

print(model.layers)
print(model.layers[0].get_weights())

a = model.layers[0].get_weights()[0][0,0]
print(a)

print("time to double", np.log(2)/a)

X = np.array(X).flatten()
Y=np.array(Y)
denomiator = X.dot(Y) -X.mean() * X.sum()
a = (X.dot(Y) - Y.mean()*X.sum()) / denomiator
b=( Y.mean()*X.dot(X) -X.mean() )
print(a, b)
print("time to double", np.log(2)/a)
