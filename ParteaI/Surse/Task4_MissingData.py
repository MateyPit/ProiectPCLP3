import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('train.csv')

lines = len(df)

# Numarul de valori lipsa pentru fiecare coloana
missing_data_cols = df.isnull().sum()

# Doar coloanele cu valori lipsa
cols = missing_data_cols[missing_data_cols > 0]

# Lista cu numele acestor coloane
list_cols = list(cols.index)

for i in range(0, len(list_cols)):
    print(f'Percent of missing data for column "{list_cols[i]}": {round(cols.iloc[i] / lines * 100, 2)}%')
    # Numarul de celule goale din coloana 'list_cols[i]' pentru care pasagerul a supravietuit
    survival_stats = df.loc[df['Survived'] == 1, list_cols[i]].isnull().sum()
    print(f'People with missing data in column "{list_cols[i]}" who have survived: {round(survival_stats / cols.iloc[i] * 100, 2)}%')
    # Ca mai sus, pentru pasagerii decedati
    deceased_stats = df.loc[df['Survived'] == 0, list_cols[i]].isnull().sum()
    print(f'People with missing data in column "{list_cols[i]}" who have died: {round(deceased_stats / cols.iloc[i] * 100, 2)}%')
    print()

