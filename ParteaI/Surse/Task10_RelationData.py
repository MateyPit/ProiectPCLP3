import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('train.csv')

# Coloana cu numarul total de membrii
df['Family members'] = df['SibSp'] + df['Parch']

family_hist = plt.figure()
sns.histplot(data = df, x = 'Family members', hue = 'Survived', palette = 'bright', stat = 'percent')
plt.title("Survival rate based on family size")
family_hist.savefig("Task10_FamilyGraph")

df = pd.read_csv('train.csv')

relation_graph = sns.catplot(data = df.head(100), x = 'Pclass', y = 'Fare', hue = 'Survived', kind = 'swarm')
plt.title("Relationship between paid fare, class and rate of survival")
relation_graph.savefig("Task10_RelationGraph")
