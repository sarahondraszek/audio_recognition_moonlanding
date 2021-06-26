from preprocessing_and_training.preprocess_with_yaml import save_data_to_array


# Save data to array file first -> has to be done only once for a model!
def create_arrays(feature_dim=40):
    """
    Feature dimension is set here but can be modified in the run-pipeline

    :param feature_dim: Has to be the same as the maximum length of the MFCCs
    :return: None
    """
    save_data_to_array(max_len=feature_dim)
