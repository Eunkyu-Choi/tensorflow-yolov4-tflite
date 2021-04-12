import tensorflow as tf
from tensorflow.keras import models

model = models.load_model('./checkpoints/yolov4-tiny')
tf.saved_model.save(model, './checkpoints/yolov4-tiny')
# model.summary()