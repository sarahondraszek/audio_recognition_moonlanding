from preprocess_with_yaml import save_data_to_array


# Save data to array file first
# Feature dimension is set here but can be modified in the run-pipeline
def create_arrays(feature_dim=40):
    save_data_to_array(max_len=feature_dim)


# create_arrays()
