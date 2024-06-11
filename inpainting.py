#inpainting model:
#source: https://github.com/jazzsaxmafia/Inpainting

import tensorflow as tf
from tensorflow.keras import layers
import numpy as np
import os
import pickle
import ipdb

## ARGUMENTS
EPOCHS = 300
LEARNING_RATE = 0.001
WEIGHT_DECAY = 0.00001
MOMENTUM = 0.9
BATCH_SIZE = 64

EXAMPLES_TO_GENERATE = 8
IMAGE_HEIGHT = 256
IMAGE_WIDTH = 256
BATCH_SIZE = 8 
TF_RECORD_PATH = "output.tfrecord"
OUTPUT_PATH = "../imgpainting/results/"

noise_dim = 100
seed = tf.random.normal([EXAMPLES_TO_GENERATE, noise_dim])



    
def generator_block(model, num_filters, kernel, num_strides):
    model.add(layers.conv2D(num_filters, kernel, strides=num_strides, padding='same', use_bias=False))
    model.add(layers.leaky_relu(layers.BatchNormalization()))
    return model

def deconv_block(model, num_filters, kernel, num_strides):
    model.add(layers.Conv2DTranspose(num_filters, kernel, strides=num_strides, padding='same', use_bias=False))
    model.add(layers.leaky_relu(layers.BatchNormalization()))
    return model

def discriminator_block(model, num_filters, kernel, num_strides):
    model.add(layers.Conv2D(num_filters, kernel, strides=num_strides, padding='same'))
    
    #convolution
    #leaky relu


def make_generator():
    generator = tf.keras.Sequential()
    generator.add(generator_block(256, (4, 4), 2))
    generator.add(generator_block(128, (4, 4), 2))
    generator.add(generator_block(64, (4, 4), 2))
    generator.add(generator_block(32, (4, 4), 2))

    generator.add(deconv_block(512, (4, 4), 2))
    generator.add(deconv_block(256, (4, 4), 2))

    


def make_discriminator(images, is_train, reuse = None):
        pass

def train():
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)
    


