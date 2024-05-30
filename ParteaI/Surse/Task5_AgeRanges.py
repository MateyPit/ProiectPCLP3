import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('train.csv')

# ======== Task 5 ========

# Cea mai mare varsta
max_age = int(df['Age'].max())

# Celulele impartite in fiecare interval
ranges = [(df['Age'] <= 20), (df['Age'] > 20) & (df['Age'] <= 40), (df['Age'] > 40) & (df['Age'] <= 60), (df['Age'] > 60)]

# Indexul pentru interval
indexes = [0, 1, 2, 3]

# Construim noua coloana cu datele de mai sus, cu 'NaN' default
df['Age Range'] = np.select(ranges, indexes, np.nan)

# Numarul de celule pentru fiecare interval
sum_category = [(df['Age Range'] == 0).sum(), (df['Age Range'] == 1).sum(), (df['Age Range'] == 2).sum(), (df['Age Range'] == 3).sum()]

last_categpry = '61 - ' + str(max_age)

# Intervalele pentru graf
graph_ranges = ['0 - 20', '21 - 40', '41 - 60', last_categpry]

range_bar = plt.figure()
plt.bar(graph_ranges, sum_category)
plt.title("Passengers divided by age ranges")
plt.xlabel("Age ranges")
plt.ylabel("Number of Passengers")
range_bar.savefig("Task5_RangeGraph")

df.to_csv('../Date/task5_train')

# ======== Task 6 ========

men_rates = []

# Lista cu numarul de barbati care au supravietuit din fiecare interval de varsta
for i in indexes:
    men_rates.append(((df['Age Range'] == i) & (df['Sex'] == 'male') & (df['Survived'] == 1)).sum())

for i in indexes:
    # Numarul de barbati din fiecare interval
    total_men = ((df['Age Range'] == i) & (df['Sex'] == 'male')).sum()
    # Rata de supravietuire
    men_rates[i] = round(men_rates[i] / total_men * 100, 2)

print('Chance of survival for men in different age ranges:')
for i in indexes:
    print(f'Men who were {graph_ranges[i]} years old: {men_rates[i]}%')

men_survival = plt.figure()
plt.bar(graph_ranges, men_rates)
plt.title('Rate of survival for men in different age groups')
plt.ylim(0, 100)
plt.ylabel('Rate of survival')
plt.xlabel('Age ranges for men')
men_survival.savefig("Task6_MenSurvivalGraph")

