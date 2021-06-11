import tensorflow.keras
from preprocessing_and_training.train import reshape_and_predict
import glob

""" Script for prediction - testing and importing the trained model from train.py """


def make_predictions(file_list, model, is_game=False):
    """ Predictions with model that is locally saved

    :param file_list: path to files we want to predict
    :param model: Trained model for our predictions
    :return: None """
    temp_list = []
    for wav_file in glob.glob(file_list):
        temp_list.append(reshape_and_predict(filepath=wav_file, saved_model=model, is_game=is_game))

    return temp_list


def make_single_prediction(wav_file, model, is_game):
    """ Predictions with model that is locally saved

    :param wav_file: wav-file we want to predict
    :param model: Trained model for our predictions
    :return: None """

    return reshape_and_predict(filepath=wav_file, saved_model=model, is_game=is_game)
