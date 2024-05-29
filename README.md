# Proiect PCLP3

#### NICOLESCU Petre - 314CD

Acest proiect are ca obiectiv prelucrarea setului de date "Titanic", care contine o varietate 
de informatii despre pasagerii Titanicului, precum numele, varsta, tariful platit, numarul de
rude, etc. Scopul final este obtinerea unor statistici care au potentialul de a prezice sansa
de supravietuire a unui individ de pe nava Titanic. In Partea I, ne vom axa pe calcularea acestor
procentaje, vom studia modul in care diferitele caracteristici ale pasagerilor afecteaza aceste
rezultate si vom incerca sa tragem cateva concluzii pe tiparelor identificate.

Primul pas este stocarea datelor din fisierul oferit drept suport, `train.csv`, prin intermediul
unui ***Dataframe Pandas***:
```
df = pd.read_csv('train.csv')
```

## Cerinta 1

In prima cerinta, se cer cateva informatii de baza despre dataframe-ul creat: Numarul de linii
(_891_), numarul de coloane (_12_), numarul de linii duplicat, tipurile de date pentru fiecare
coloana si numarul de valori lipsa din fiecare coloana (In cazul nostru, doar coloanele *'Age'*,
*'Cabin'* si *'Embarked'* au valori lipsa):
> Age: 177  
> Cabin: 687  
> Embarked: 2  

Pentru afisarea valorilor lipsa, folosim functia `isnull()`:
```
print('Number of missing values for each column: ')  
print(df.isnull().sum())  
```
Pentru afisarea numarului de linii duplicat, folosim functia `duplicated()`:
```
print(f'Number of duplicated rows: {df.duplicated().sum()}')
```

## Cerinta 2

A doua cerinta propune calcularea unor statistici bazate pe cate o singura coloana.
Pentru coloana *'Survived'*, calculam suma valorilor din celule si calculam procentajul, rotunjit
cu doua zecimale:
```
nr_survivors = round(df['Survived'].sum() / nr_lines * 100, 2)
nr_deceased = 100 - nr_survivors;
```
> OBSERVATIE: Aceasta modalitate functioneaza deoarece aceasta coloana are doar valori de 0 si 1, unde
> 1 semnifica faptul ca pasagerul a supravietuit

Acesta este graful de tip `bar` care ilustreaza rata de supravietuire:

![Survival Graph!](/ParteaI/Surse/Task2_SurvivalGraph.png "Survival Graph")

> Survivors: 38.38%  
> Deceased: 61.62%

Pentru calcularea statisticilor pentru coloanele *'Pclass'* si *'Sex'*, nu putem folosi acceasi
tehnica, ci conditionam coloanele. Spre exemplu, pentru obtinerea procentului de barbati, folosim
comanda:
```
males = round((df['Sex'] == 'male').sum() / nr_lines * 100, 2)
```

Graful pentru procentul de barbati de femei este:

![Gender Graph!](/ParteaI/Surse/Task2_GenderGraph.png "Gender Graph")

> Percentage of males: 64.76%  
> Percentage of females: 35.24%

Si in final, graful care imparte pasagerii dupa clasa:

![Class Graph!](/ParteaI/Surse/Task2_ClassGraph.png "Class Graph")

> Third class passengers: 55.11%  
> Second class passengers: 20.65%  
> First class passengers: 24.24%  

## Cerinta 3

In aceasta sectiune, focusul se muta pe reprezentarea anumitor distributii de frecvente pentru
informatiile din dataframe. Pentru aceste ilustrari, folosim ***histograme***, folosind ca 
suport libraria *Matplotlib*:
```
import matplotlib.pyplot as plt
```

Tot ce avem de facut este sa extragem coloana dorita, aplicam `plt.hist()` asupra acesteia 
si schimbam cateva caracteristici ale grafului, precum titlul, numele si limitele pentru axele
Ox si Oy.

1. Histograma ce ilustreaza distributia varstelor

![Age Histogram!](/ParteaI/Surse/Task3_AgeHistogram.png "Age Histogram")

2. Histograma pentru tarifele platite de pasageri:

![Fare Histogram!](/ParteaI/Surse/Task3_FareHistogram.png "Fare Histogram")

3. Histograma coloanei 'SibSp' (Siblings/Spouses):

![SibSp Histogram!](/ParteaI/Surse/Task3_SibSpHistogram.png "SibSp Histogram")

3. Histograma coloanei 'Parch' (Parents/Children):

![Parch Histogram!](/ParteaI/Surse/Task3_ParchHistogram.png "Parch Histogram")

## Cerinta 4

In cadrul acestei cerinte, identificam coloanele cu valori lipsa (*Nan*), iar apoi construim
un obiect `cols` care retine numele acestor coloane si numarul de valori lipsa, precum si o lista
`list_cols` care retine doar numele coloanelor necesare.
Primul oara, afisam procentul de celule goale din acea coloana:
```
# Numarul de celule goale / numarul de linii * 100
print(f'Percent of missing data for column "{list_cols[i]}": {round(cols.iloc[i] / lines * 100, 2)}%')
```
Mai departe, calculam numarul de persoane ale caror detalii lipsesc din coloana curenta, dar au 
supravietuit/murit:
```
survival_stats = df.loc[df['Survived'] == 1, list_cols[i]].isnull().sum()
deceased_stats = df.loc[df['Survived'] == 0, list_cols[i]].isnull().sum()
```
Iar apoi calculam procentul in functie de numarul total de celule goale din acea coloana. Astfel, 
obtinem urmatoarele rezultate:

> Percent of missing data for column "Age": 19.87%
> People with missing data in column "Age" who have survived: 29.38%
> People with missing data in column "Age" who have died: 70.62%
>
> Percent of missing data for column "Cabin": 77.1%
> People with missing data in column "Cabin" who have survived: 29.99%
> People with missing data in column "Cabin" who have died: 70.01%
>
> Percent of missing data for column "Embarked": 0.22%
> People with missing data in column "Embarked" who have survived: 100.0%
> People with missing data in column "Embarked" who have died: 0.0%
