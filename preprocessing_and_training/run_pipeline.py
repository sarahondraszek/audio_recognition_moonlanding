from predict import make_predictions
from preprocess_with_yaml import get_labels
from create_arrays import create_arrays
import keras
import glob
import pandas


""" THIS SCRIPT IS A MANAGING TOOL FOR RUNNING THE DIFFERENT COMPONENTS """

""" Set parameters in the files first """

sample_path = './command_sampleset/Befehle_Elsaesser/'
sample_list = glob.glob(sample_path)
model = keras.models.load_model('./model')

# If you need to create arrays from your audio-data first, please use the following method
# Feature dimensions are pre-set to 11, can be changed and given manually in the method
# Involved are: preprocess_with_yaml.py and create_arrays.py
# Remember changing the paths in the preprocess_with_yaml.py

# create_arrays()

# If you need to train the model, please use the train.py script so you can save it locally
# Involved are preprocess_with_yaml.py and train.py

# When you want to test/predict samples, use the following method -> Method takes path for files as param,
# makes file with output

output_matrix = {}
for label in get_labels()[0]:
    output_matrix[label] = make_predictions(sample_path + label + '/*.wav', model)

print(output_matrix)
df = pandas.DataFrame.from_dict(output_matrix, orient='index')
df.to_csv('./output_testing/output_predictions.csv')