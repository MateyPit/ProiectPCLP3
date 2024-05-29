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
coloana si numarul de valori lipsa din fiecare coloana (In cazul nostru, doar coloanele 'Age',
'Cabin' si 'Embarked' au valori lipsa):
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
> OBS: Aceasta modalitate functioneaza deoarece aceasta coloana are doar valori de 0 si 1, unde
> 1 semnifica faptul ca pasagerul a supravietuit


![This is a graph!](/ParteaI/Task3_AgeHistogram.png "Age Histogram")
