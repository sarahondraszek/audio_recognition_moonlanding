from create_arrays import *
from preprocess_with_yaml import *
from train import *
from predict import *

""" THIS SCRIPT IS A MANAGING TOOL FOR RUNNING THE DIFFERENT COMPONENTS """

""" THIS PART IS FOR TRAINING AND PREPROCESSING """

""" Setting parameters first """

# If you need to create arrays from your audio-data first, please use the following method
# Feature dimensions are pre-set to 11, can be changed and given manually in the method
# Involved are: preprocess_with_yaml.py and create_arrays.py

# create_arrays()

# If you need to train the model, please use the train.py script so you can save it locally
# Involved are preprocess_with_yaml.py and train.py

# When you want to test/predict samples, use the following method -> Method takes path for files

make_predictions('/home/ondraszek/scripts/Befehle_Elsaesser/*.wav')


