import librosa
import yaml as ym
import os
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
import numpy as np
from tqdm import tqdm

""" This script is for preprocessing the different files, including our test set for creating the language model,
as well as for the later used sample set that also has to be transformed """

DATA_PATH_WAV = "/media/nfs/data/speech-commands/wav/"
DATA_PATH_NPY = "/home/ondraszek/scripts/data/numpy/"
yaml = 'yaml-config.yaml'


# Input: YAML-config file with our labels
# Output: Tuple (Label, Indices of the labels, one-hot encoded labels)

def get_labels(yaml=yaml):
    yaml_file = open(yaml)
    parsed_yaml_file = ym.load(yaml_file, Loader=ym.FullLoader)
    labels = []
    for x in parsed_yaml_file["label_dict"].values():
        labels.append(x)
    label_indices = np.arange(0, len(labels))
    return labels, label_indices, to_categorical(label_indices)


# Function to convert wav-files to MFCCs with max_length manually set to 50, a sampling rate of 16kHz and a n_fft of 512
def wav2mfcc(file_path, max_len=40):
    wave, sr = librosa.load(file_path, mono=True, sr=None)
    wave = wave[::3]
    mfcc = librosa.feature.mfcc(wave, sr=16000, n_fft=512)

    # If maximum length exceeds mfcc lengths then pad the remaining ones,
    # meaning the arrays will be made the same length and missing data will be filled with 0s
    if max_len > mfcc.shape[1]:
        pad_width = max_len - mfcc.shape[1]
        mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')

    # Else cutoff the remaining parts
    else:
        mfcc = mfcc[:, :max_len]

    return mfcc


# Saving data from wav2mfcc in numpy-arrays in files on described path
def save_data_to_array(path=DATA_PATH_WAV, max_len=40):
    labels, _, _ = get_labels(yaml)

    for label in labels:
        # Init mfcc vectors
        mfcc_vectors = []

        wavfiles = [path + label + '/' + wavfile for wavfile in os.listdir(path + '/' + label)]
        for wavfile in tqdm(wavfiles, "Saving vectors of label - '{}'".format(label)):
            mfcc = wav2mfcc(wavfile, max_len=max_len)
            mfcc_vectors.append(mfcc)
        np.save('/home/ondraszek/scripts/data/numpy/' + label + '.npy', mfcc_vectors)


# Method to obtain training test set in one array
def get_train_test(split_ratio=0.6, random_state=42):
    # Get available labels
    labels, indices, _ = get_labels(yaml)

    # Getting first arrays
    X = np.load(DATA_PATH_NPY + labels[0] + '.npy')
    y = np.zeros(X.shape[0])

    # Append all of the dataset into one single array, same goes for y
    for i, label in enumerate(labels[1:]):
        x = np.load(DATA_PATH_NPY + label + '.npy')
        X = np.vstack((X, x))
        y = np.append(y, np.full(x.shape[0], fill_value=(i + 1)))

    assert X.shape[0] == len(y)

    return train_test_split(X, y, test_size=(1 - split_ratio), random_state=random_state, shuffle=True)


# Method for dataset preparation, without downsampling to improve performance
def prepare_dataset(path=DATA_PATH_WAV):
    labels, _, _ = get_labels(yaml)
    data = {}
    for label in labels:
        data[label] = {}
        data[label]['path'] = [path + label + '/' + wavfile for wavfile in os.listdir(path + '/' + label)]

        vectors = []

        for wavfile in data[label]['path']:
            wave, sr = librosa.load(wavfile, mono=True, sr=None)
            # Downsampling
            # wave = wave[::3]
            mfcc = librosa.feature.mfcc(wave, sr=16000, n_fft=512)
            vectors.append(mfcc)

        data[label]['mfcc'] = vectors

    return data

# Method for loading dataset in the training script
def load_dataset(path=DATA_PATH_NPY):
    data = prepare_dataset(path)

    dataset = []

    for key in data:
        for mfcc in data[key]['mfcc']:
            dataset.append((key, mfcc))

    return dataset[:100]
