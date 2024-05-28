import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('train.csv')

# Task 5

max_age = int(df['Age'].max())

ranges = [(df['Age'] <= 20), (df['Age'] > 20) & (df['Age'] <= 40), (df['Age'] > 40) & (df['Age'] <= 60), (df['Age'] > 60)]

indexes = [0, 1, 2, 3]

df['Age Range'] = np.select(ranges, indexes)

sum_category = [(df['Age Range'] == 0).sum(), (df['Age Range'] == 1).sum(), (df['Age Range'] == 2).sum(), (df['Age Range'] == 3).sum()]

last_categpry = '61 - ' + str(max_age)

graph_ranges = ['0 - 20', '21 - 40', '41 - 60', last_categpry]

range_bar = plt.figure()
plt.bar(graph_ranges, sum_category)
plt.title("Passengers divided by age ranges")
plt.xlabel("Age ranges")
plt.ylabel("Number of Passengers")
range_bar.savefig("RangeGraph")

