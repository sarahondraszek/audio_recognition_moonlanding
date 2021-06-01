import keras
from train import reshape_and_predict
import glob

""" Script for prediction - testing and importing the trained model from train.py """


def make_predictions(file_list, model):
    """ Predictions with model that is locally saved

    :param file_list: path to files we want to predict
    :param model: Trained model for our predictions
    :return: None """
    temp_list = []
    for wav_file in glob.glob(file_list):
        temp_list.append(reshape_and_predict(filepath=wav_file, saved_model=model))

    return temp_list


def make_single_prediction(wav_file, model):

    return reshape_and_predict(filepath=wav_file, saved_model=model)
