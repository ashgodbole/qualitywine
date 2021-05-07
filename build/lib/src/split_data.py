#split raw data
#save in it data/processed folder

import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params

def split_and_saved_data(config_path):
    config = read_params(config_path)
    # get all the path form params.yaml file
    # here we need the path for storing the train and test data
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]

    df = pd.read_csv(raw_data_path, sep=",") # read raw data path
    train, test = train_test_split(df,test_size=split_ratio, random_state = random_state)
    train.to_csv(train_data_path, sep=",",index=False, encoding='utf-8')  # save train data into file
    test.to_csv(test_data_path, sep=",",index=False, encoding='utf-8')  # save test data into file

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="C:/Users/ashle/Documents/qualitywine/params.yaml")
    parsed_args = args.parse_args()
    path = parsed_args.config
    split_and_saved_data(config_path=path)


