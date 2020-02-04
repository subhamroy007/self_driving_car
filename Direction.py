# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:36:44 2019

@author: Saikat
"""

import keras
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten 
from keras.layers import Dense
from keras.models import model_from_json
classifier = Sequential()

classifier.add(Convolution2D(64,kernel_size = (4,4),input_shape = (32,32,3),activation = 'relu'))

classifier.add(MaxPooling2D(pool_size = (4,4)))

classifier.add(Convolution2D(32,kernel_size = (3,3),activation = 'relu'))

classifier.add(MaxPooling2D(pool_size = (2,2)))

classifier.add(Flatten())

classifier.add(Dense(output_dim = 64, activation = 'relu'))
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 4, activation = 'softmax'))

classifier.compile(optimizer = 'adam',loss = 'categorical_crossentropy',metrics = ['accuracy'])

from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory('dataset',
                                                    target_size=(32, 32),
                                                    batch_size=32,
                                                    class_mode='categorical')


classifier.fit_generator(train_generator,
        steps_per_epoch=1290,
        epochs=20)
model_json=classifier.to_json()
with open("model.json","w") as json_file:
    json_file.write(model_json)
classifier.save_weights("model.h5")
