import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('train.csv')

lines = len(df)

missing_data_cols = df.isnull().sum()

cols = missing_data_cols[missing_data_cols > 0]

list_cols = list(cols.index)

for i in range(0, len(list_cols)):
    try:
        mean_value = round(df.loc[df['Survived'] == 1, list_cols[i]].mean())
        print(f'Average value for "{list_cols[i]}": {mean_value}')
    except TypeError:
        mean_value = (df.loc[df['Survived'] == 1, list_cols[i]]).mode()[0]
        print(f'Most common value for "{list_cols[i]}": {mean_value}')
    df[list_cols[i]] = df[list_cols[i]].fillna(mean_value)

df.to_csv('../Date/task8_train')