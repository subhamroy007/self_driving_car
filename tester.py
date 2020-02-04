
# MLP for Pima Indians Dataset Serialize to JSON and HDF5
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy as np
import os
import cv2




json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")

loaded_model.compile(optimizer = 'adam',loss = 'categorical_crossentropy',metrics = ['accuracy'])

img = cv2.imread('59.png', cv2.IMREAD_UNCHANGED)
 
# resize image
img = cv2.resize(img,(32,32))
img = np.reshape(img,[1,32,32,3])

im_pred = loaded_model.predict(img)

print(im_pred[0])
