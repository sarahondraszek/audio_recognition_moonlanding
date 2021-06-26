import numpy as np
import tensorflow.keras
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
# from keras.utils import to_categorical
from preprocessing_and_training.preprocess_with_yaml import wav2mfcc, get_labels
import tensorflow as tf

""" Script for training the model for chosen speech commands """

# Second dimension of the feature is dim2

feature_dim_2 = 40

# Feature dimension

feature_dim_1 = 20
channel = 1
epochs = 150
batch_size = 100
verbose = 1
num_classes = 8


def get_model():
    """
    # Trains the model

    :return: Trained keras model
    """
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(2, 2), activation='relu', input_shape=(feature_dim_1, feature_dim_2, channel)))
    model.add(Conv2D(48, kernel_size=(2, 2), activation='relu'))
    model.add(Conv2D(120, kernel_size=(2, 2), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.40))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer='adam',
                  metrics=['accuracy'])
    return model


def reshape_and_predict(filepath, saved_model, is_game):
    """
    Predictions and reshaping for test data

    :param filepath: Path of sample wav-data that needs to be reshaped
    :param saved_model: Trained model, can be loaded from storage
    :return: Command prediction for the input wav-file
    """
    sample = wav2mfcc(filepath)
    sample_reshaped = sample.reshape(1, feature_dim_1, feature_dim_2, channel)
    return get_labels(is_game=is_game)[0][
        np.argmax(saved_model.predict(sample_reshaped))
    ]
