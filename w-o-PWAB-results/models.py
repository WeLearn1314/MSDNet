from keras.models import Model
from keras.layers import Input, Add,Subtract, PReLU, Conv2DTranspose, \
    Concatenate, MaxPooling2D, UpSampling2D, Dropout, concatenate, GlobalAveragePooling2D,\
    Reshape, Dense, Multiply, Activation, BatchNormalization
from keras.layers.convolutional import Conv2D
from keras import backend as K
import tensorflow as tf
import os

def MSDNet():
    inpt = Input(shape=(None,None,1))
    #layer 1
    x = Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding='same', kernel_initializer="he_normal")(inpt)
    x = PReLU(shared_axes=[1,2])(x)
    s0 = x
    x = Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding='same', kernel_initializer="he_normal")(x)
    x = PReLU(shared_axes=[1,2])(x)
    s1 = x
    for i in range(5):
        x0 = Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding='same', dilation_rate=(1,1), kernel_initializer="he_normal")(s1)
        x0 = PReLU(shared_axes=[1,2])(x0)
        x1 = Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding='same', dilation_rate=(3,3), kernel_initializer="he_normal")(s1)
        x1 = PReLU(shared_axes=[1,2])(x1)
        x2 = Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding='same', dilation_rate=(5,5), kernel_initializer="he_normal")(s1)
        x2 = PReLU(shared_axes=[1,2])(x2)
        x01 = concatenate([x0,x1],axis=-1)
        x01 = Conv2D(filters=64, kernel_size=(1,1), strides=(1,1), padding='same', kernel_initializer="he_normal")(x01)
        x01 = PReLU(shared_axes=[1,2])(x01)
        x012 = concatenate([x01,x2],axis=-1)
        x012 = Conv2D(filters=64, kernel_size=(1,1), strides=(1,1), padding='same', kernel_initializer="he_normal")(x012)
        x012 = PReLU(shared_axes=[1,2])(x012)
        # x0 = Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding='same', dilation_rate=(1,1), kernel_initializer="he_normal")(s1)
        # x0 = PReLU(shared_axes=[1,2])(x0)
        # x1 = Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding='same', dilation_rate=(3,3), kernel_initializer="he_normal")(s1)
        # x1 = PReLU(shared_axes=[1,2])(x1)
        # x2 = Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding='same', dilation_rate=(5,5), kernel_initializer="he_normal")(s1)
        # x2 = PReLU(shared_axes=[1,2])(x2)
        # x01 = concatenate([x0,x1],axis=-1)
        # x01 = Conv2D(filters=64, kernel_size=(1,1), strides=(1,1), padding='same', kernel_initializer="he_normal")(x01)
        # x01 = PReLU(shared_axes=[1,2])(x01)
        # x012 = concatenate([x0,x1,x2],axis=-1)
        # x012 = Conv2D(filters=64, kernel_size=(1,1), strides=(1,1), padding='same', kernel_initializer="he_normal")(x012)
        # x012 = PReLU(shared_axes=[1,2])(x012)
        # pw = Conv2D(filters=1, kernel_size=(3,3), strides=(1,1), padding='same', kernel_initializer="he_normal")(x012)
        # pw = PReLU(shared_axes=[1,2])(pw)
        # pw = Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding='same', kernel_initializer="he_normal")(pw)
        # pw = Activation('sigmoid')(pw)
        # pw = Multiply()([x012, pw])
        s1 = Add()([x012, s1])
    x = Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding='same', kernel_initializer="he_normal")(s1)
    x = PReLU(shared_axes=[1,2])(x)
    x = Add()([x, s0])
    x = Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding='same', kernel_initializer="he_normal")(x)
    x = PReLU(shared_axes=[1,2])(x)
    x = Conv2D(filters=1, kernel_size=(3,3), strides=(1,1), padding='same', kernel_initializer="he_normal")(x)  # gray is 1 color is 3
    o = Subtract()([inpt, x])
    model = Model(inputs=inpt, outputs=o)
    # model.summary()
    return model