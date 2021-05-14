import keras
from train import reshape_and_predict
import glob

""" Script for prediction - testing and importing the trained model from train.py """


def make_predictions(file_list):
    model = keras.models.load_model('/home/ondraszek/scripts/data/model')
    print(model.summary())

    for wav_file in glob.glob(file_list):
        print(wav_file, reshape_and_predict(wav_file, model=model))
