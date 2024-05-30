import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('train.csv')

# Numarul de varste stiute
total_ages = len(df['Age']) - df['Age'].isnull().sum()

# Numarul de copii
total_children = (df['Age'] < 18).sum()

# Numarul de adulti
total_adults = (df['Age'] >= 18).sum()

# Procentajul copil / adult
children_stats = total_children / total_ages * 100

adult_stats = total_adults / total_ages * 100

print(f'Percentage of children passengers: {round(children_stats, 2)}%')
print(f'Percentage of adult passengers: {round(adult_stats, 2)}%')

# Ratele de supravietuire pentru fiecare
survived_children = ((df['Age'] < 18) & (df['Survived'] == 1)).sum() / total_children * 100
survived_adults = ((df['Age'] >= 18) & (df['Survived'] == 1)).sum() / total_adults * 100

print(f'Rate of survival for children: {round(survived_children, 2)}%')
print(f'Rate of survival for adults: {round(survived_adults, 2)}%')

age_groups = ['Children', 'Adults']
group_percentage = [round(survived_children, 2), round(survived_adults, 2)]

child_survival = plt.figure()
plt.bar(age_groups, group_percentage)
plt.title("Rate of survival for children and adults")
plt.ylim(0, 100)
plt.xlabel("Age groups")
plt.ylabel("Rate of survival")
child_survival.savefig("Task7_ChildGraph")