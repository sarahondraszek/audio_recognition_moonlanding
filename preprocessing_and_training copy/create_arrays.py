from preprocess_with_yaml import *


# Save data to array file first
# =====
# auskommentiert. die vorberechneten npy-dateien (jeweils mfcc-arrays) liegen unter /media/nfs/speech-commands/npy
# =====

# Feature dimension is set here but can be modified in the run-pipeline
def create_arrays(feature_dim=11):
    save_data_to_array(max_len=feature_dim)
