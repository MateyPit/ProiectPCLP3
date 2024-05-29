import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('train.csv')

df['Name'] = df['Name'].str.split(',')

for i in range(len(df)):
    df.loc[i, 'Name'] = df['Name'][i][1]

df['Name'] = df['Name'].str.split('.')

for i in range(len(df)):
    df.loc[i, 'Name'] = df['Name'][i][0]

titles = df['Name'].unique()

title_number = []

for i in range(len(titles)):
    title_number.append(round((df['Name'] == titles[i]).sum()))

title_graph = plt.figure(figsize=(16, 6))
plt.bar(titles, title_number)
plt.title("Passengers split by title")
plt.xlabel("Titles")
plt.ylabel("Number of passengers")
plt.tight_layout()
title_graph.savefig("TitleGraph")
