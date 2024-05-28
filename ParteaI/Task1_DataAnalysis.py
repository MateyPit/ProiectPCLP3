import pandas as pd

df = pd.read_csv('train.csv')

print('Analysis of data within train.csv:')

print(f'Number of columns: {len(df.columns)}')

print(f'Number of lines: {len(df)}')

print('Data types of each row:')
print(df.dtypes)

print('Number of missing values for each column: ')
print(df.isnull().sum())

print(f'Number of duplicated rows: {df.duplicated().sum()}')