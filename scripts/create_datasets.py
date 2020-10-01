import pandas as pd
from sklearn.model_selection import train_test_split
import re
import os
import sys

input_path = os.path.join(sys.path[0], "../datasets/dataset2/compiled.txt")
output_path = os.path.join(sys.path[0], "../datasets/dataset2")

df = []

with open(input_path, 'r') as f:
    for line in f:
        df.append(line)

train_test_ratio = 0.9
train_valid_ratio = 7/9
df_full_train, df_test = train_test_split(df, train_size = train_test_ratio, random_state = 1)
df_train, df_valid = train_test_split(df_full_train, train_size = train_valid_ratio, random_state = 1)

def build_dataset(df, dest_path):
    f = open(dest_path, 'w')
    data = ''
    for line in df:
        data += line
    f.write(data)

build_dataset(df_train, os.path.join(output_path, 'train.txt'))
build_dataset(df_valid, os.path.join(output_path, 'valid.txt'))
build_dataset(df_test, os.path.join(output_path, 'test.txt'))