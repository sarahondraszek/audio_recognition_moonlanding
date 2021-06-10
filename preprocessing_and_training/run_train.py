from preprocessing_and_training.train import get_model, feature_dim_1, feature_dim_2, channel, \
    batch_size, verbose, epochs
import tensorflow as tf
from preprocessing_and_training.preprocess_with_yaml import get_train_test

""" Save the model in the correct folder so we can later load it - Uncomment when in need of a need model """
""" First part is the fetching and shaping of the data, shall be removed when needed """
# Loading train set and test set

X_train, X_test, y_train, y_test = get_train_test()

# Reshaping to perform 2D convolution

X_train = X_train.reshape(X_train.shape[0], feature_dim_1, feature_dim_2, channel)
X_test = X_test.reshape(X_test.shape[0], feature_dim_1, feature_dim_2, channel)

y_train_hot = tf.keras.utils.to_categorical(y_train)
y_test_hot = tf.keras.utils.to_categorical(y_test)

model = get_model()
model.fit(X_train, y_train_hot, batch_size=batch_size, epochs=epochs, verbose=verbose,
          validation_data=(X_test, y_test_hot))
# model.save('./model')