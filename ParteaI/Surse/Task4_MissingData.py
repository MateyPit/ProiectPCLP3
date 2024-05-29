import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('train.csv')

lines = len(df)

missing_data_cols = df.isnull().sum()

cols = missing_data_cols[missing_data_cols > 0]

list_cols = list(cols.index)

for i in range(0, len(list_cols)):
    print(f'Percent of missing data for column "{list_cols[i]}": {round(cols.iloc[i] / lines * 100, 2)}%')
    survival_stats = df.loc[df['Survived'] == 1, list_cols[i]].isnull().sum()
    print(f'People with missing data in column "{list_cols[i]}" who have survived: {round(survival_stats / cols.iloc[i] * 100, 2)}%')
    deceased_stats = df.loc[df['Survived'] == 0, list_cols[i]].isnull().sum()
    print(f'People with missing data in column "{list_cols[i]}" who have died: {round(deceased_stats / cols.iloc[i] * 100, 2)}%')
    print()

