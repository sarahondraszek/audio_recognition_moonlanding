from preprocessing_and_training.preprocess_with_yaml import save_data_to_array


# Save data to array file first
def create_arrays(feature_dim=40):
    """
    Feature dimension is set here but can be modified in the run-pipeline

    :param feature_dim: Has to be the same as the maximum length of the MFCCs
    :return: None
    """
    save_data_to_array(max_len=feature_dim)

# Uncomment to let the script make new arrays, only needed if data has changed
# create_arrays()
