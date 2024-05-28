import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('train.csv')

nr_lines = len(df)
nr_survivors = round(df['Survived'].sum() / nr_lines * 100, 2)
nr_deceased = 100 - nr_survivors;
print('Percentages for given data:')
print(f'Survivors: {nr_survivors}%')
print(f'Deceased: {nr_deceased}%')

third_class = round((df['Pclass'] == 3).sum() / nr_lines * 100, 2)
second_class = round((df['Pclass'] == 2).sum() / nr_lines * 100, 2)
first_class = round((df['Pclass'] == 1).sum() / nr_lines * 100, 2)
print(f'Third class passengers: {third_class}%')
print(f'Second class passengers: {second_class}%')
print(f'First class passengers: {first_class}%')

males = round((df['Sex'] == 'male').sum() / nr_lines * 100, 2)
females = round((df['Sex'] == 'female').sum() / nr_lines * 100, 2)
print(f'Percentage of men: {males}%')
print(f'Percentage of females: {females}%')

state = np.array(["Survivors", "Deceased"])
rates = np.array([nr_survivors, nr_deceased])

SurvivalGraph = plt.figure()
plt.bar(state, rates)
plt.title("Survival Rate")
plt.xlabel("State")
plt.ylabel("Percentage")
plt.ylim(0, 100)
SurvivalGraph.savefig('SurvivalGraph')

classes = np.array(["First Class", "Second Class", "Third Class"])
class_members = np.array([first_class, second_class, third_class])

ClassGraph = plt.figure()
plt.bar(classes, class_members)
plt.title("Passanger divided by class")
plt.xlabel("Classes")
plt.ylabel("Percentage")
plt.ylim(0, 100)
ClassGraph.savefig('ClassGraph')

sex = np.array(["Males", "Females"])
sex_percentages = np.array([males, females])

GenderGraph = plt.figure()
plt.bar(sex, sex_percentages)
plt.title("Passengers divided by sex")
plt.xlabel("Sex")
plt.ylabel("Percentage")
plt.ylim(0, 100)
GenderGraph.savefig('GenderGraph')