import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('train.csv')

ages = df["Age"]

age_hist = plt.figure()
plt.hist(ages)
plt.title("Age Distribution")
plt.xlabel("Ages")
plt.ylabel("Number of Passengers")
age_hist.savefig("Task3_AgeHistogram")

fares = df["Fare"]

fare_hist = plt.figure()
plt.hist(fares)
plt.title("Fares paid by passengers")
plt.xlabel("Fares")
plt.ylabel("Number of Passengers")
fare_hist.savefig("Task3_FareHistogram")

sibsp = df["SibSp"]

sibsp_hist = plt.figure()
plt.hist(sibsp)
plt.title("Siblings/Spouses for each passenger")
plt.xlabel("Number of siblings and spouses")
plt.ylabel("Number of Passengers")
sibsp_hist.savefig("Task3_SibSpHistogram")

parch = df["Parch"]

parch_hist = plt.figure()
plt.hist(parch)
plt.title("Parents/Children for each passenger")
plt.xlabel("Number of parents and children")
plt.ylabel("Number of Passengers")
plt.xlim(0, 5.5)
parch_hist.savefig("Task3_ParchHistogram")