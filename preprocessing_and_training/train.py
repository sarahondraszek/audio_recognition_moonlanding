from preprocessing_and_training.preprocess_with_yaml import wav2mfcc, get_labels, get_train_test
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.utils import to_categorical

""" Script for training the model for chosen speech commands """

# Second dimension of the feature is dim2

feature_dim_2 = 40

# Loading train set and test set

# X_train, X_test, y_train, y_test = get_train_test()

# Feature dimension

feature_dim_1 = 20
channel = 1
epochs = 150
batch_size = 100
verbose = 1
num_classes = 8

# Reshaping to perform 2D convolution

# X_train = X_train.reshape(X_train.shape[0], feature_dim_1, feature_dim_2, channel)
# X_test = X_test.reshape(X_test.shape[0], feature_dim_1, feature_dim_2, channel)

# y_train_hot = to_categorical(y_train)
# y_test_hot = to_categorical(y_test)




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


def reshape_and_predict(filepath, saved_model):
    """
    Predictions and reshaping for test data

    :param filepath: Path of sample wav-data that needs to be reshaped
    :param saved_model: Trained model, can be loaded from storage
    :return: Comman prediction for the input wav-file
    """
    sample = wav2mfcc(filepath)
    sample_reshaped = sample.reshape(1, feature_dim_1, feature_dim_2, channel)
    return get_labels()[0][
        np.argmax(saved_model.predict(sample_reshaped))
    ]


""" Save the model in the correct folder so we can later load it - Uncomment when in need of a need model """
# model = get_model()
# model.fit(X_train, y_train_hot, batch_size=batch_size, epochs=epochs, verbose=verbose,
#           validation_data=(X_test, y_test_hot))
# model.save('/home/ondraszek/scripts/data/model')
