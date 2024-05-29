# Proiect PCLP3

#### NICOLESCU Petre - 314CD

Acest proiect are ca obiectiv prelucrarea setului de date "Titanic", care contine o varietate 
de informatii despre pasagerii Titanicului, precum numele, varsta, tariful platit, numarul de
rude, etc. Scopul final este obtinerea unor statistici care au potentialul de a prezice sansa
de supravietuire a unui individ de pe nava Titanic. In Partea I, ne vom axa pe calcularea acestor
procentaje, vom studia modul in care diferitele caracteristici ale pasagerilor afecteaza aceste
rezultate si vom incerca sa facem cateva observatii pe baza tiparelor identificate.

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

Graful pentru procentul de barbati si de femei este:

![Gender Graph!](/ParteaI/Surse/Task2_GenderGraph.png "Gender Graph")

> Numarul de barbati este aproape dublu cel al femeilor:  
> Percentage of males: 64.76%  
> Percentage of females: 35.24%

Si in final, graful care imparte pasagerii dupa clasa:

![Class Graph!](/ParteaI/Surse/Task2_ClassGraph.png "Class Graph")

> In mod nesurprinzator, jumatate din pasageri erau din a treia clasa:  
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

> Majoritatea pasagerilor aveau intre 20 si 40 de ani

![Age Histogram!](/ParteaI/Surse/Task3_AgeHistogram.png "Age Histogram")

2. Histograma pentru tarifele platite de pasageri:

> Majoritatea pasagerilor au platit acelasi pret

![Fare Histogram!](/ParteaI/Surse/Task3_FareHistogram.png "Fare Histogram")

3. Histograma coloanei 'SibSp' (Siblings/Spouses):

> Multi pasageri au avut cel mult o singura ruda

![SibSp Histogram!](/ParteaI/Surse/Task3_SibSpHistogram.png "SibSp Histogram")

3. Histograma coloanei 'Parch' (Parents/Children):

> Multi pasageri au avut cel mult o singura ruda

![Parch Histogram!](/ParteaI/Surse/Task3_ParchHistogram.png "Parch Histogram")

## Cerinta 4

In cadrul acestei cerinte, identificam coloanele cu valori lipsa (*NaN*), iar apoi construim
un obiect `cols` care retine numele acestor coloane si numarul de valori lipsa, precum si o lista
`list_cols` care retine doar numele coloanelor necesare.
Prima oara, afisam procentul de celule goale din acea coloana:
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

## Cerinta 5

Pentru aceasta cerinta, avem de creat o noua coloana, care specifica indexul intervalului in care
se regaseste varsta unui pasager. Construim o lista in care se afla coloana *'Age'*, conditionata
de intervalele propuse. Pentru crearea noii coloane *'Age Range'*, folosim `select()`, care atribuie
valorile date, conform conditiilor oferite:
```
ranges = [(df['Age'] <= 20),
          (df['Age'] > 20) & (df['Age'] <= 40),
          (df['Age'] > 40) & (df['Age'] <= 60),
          (df['Age'] > 60)]

indexes = [0, 1, 2, 3]

# np.select(conditie, valoare, default)
df['Age Range'] = np.select(ranges, indexes, np.nan)
```

Dupa actualizarea dataframe-ului, calculam parametrii necesari pentru construirea unui graf 
(numarul de celule pentru fiecare interval, inserarea intervalelor in graf, etc.), obtinand in
final urmatoarea repartizare:

![Age Range Graph!](/ParteaI/Surse/Task5_RangeGraph.png "Age Range Graph")

In final, salvam noul dataframe intr-un fisier nou:
```
df.to_csv('../Date/task5_train')
```

## Cerinta 6

Partea aceasta presupune folosirea dataframe-ului anterior pentru calcularea ratei de
supravietuire pentru barbati in fiecare interval de varsta. Construim lista `men_rates`, 
ce contine numarul de barbati din fiecare interval care a supravietuit, iar apoi calculam
procentajul in functie de `total_men`, numarul de barbati din fiecare interval independent
de coloana *'Survived'*

```
men_rates[i] = round(men_rates[i] / total_men * 100, 2)
```

Graful care ilustreaza rata de supravietuire pentru fiecare interval:

> Tinerii care au intre 0 si 20 de ani au sansa cea mai mare

![Men Survival Graph!](/ParteaI/Surse/Task6_MenSurvivalGraph.png "Men Survival Graph")

## Cerinta 7

Considerand copiii drept pasageri cu varsta mai mica strict de 18 ani, filtram datele
pentru copii si adulti in functie de valoarea din *'Age'*:

```
# Numarul total de copii
total_children = (df['Age'] < 18).sum()
# Rata de supravietuire pentru copii
survived_children = ((df['Age'] < 18) & (df['Survived'] == 1)).sum() / total_children * 100
```
Acesta este graful care ilustreaza rezultatele obtinute:

![Children Stats Graph!](/ParteaI/Surse/Task7_ChildGraph.png "Children Stats Graph")

> Percentage of children passengers: 15.83%  
> Percentage of adult passengers: 84.17%  
> Rate of survival for children: 53.98%  
> Rate of survival for adults: 38.1%  

## Cerinta 8

Obiectivul in aceasta cerinta este sa 'umplem' celulele goale cu valorea medie din coloana
respectiva (sau cea mai comuna, pentru valori care nu sunt numerice). Procedam la fel ca la
**Cerinta 4** si calculam media cu `mean()` si valoarea cea mai comuna cu `mode()`:

> Average value for "Age": 28  
> Most common value for "Cabin": B96 B98  
> Most common value for "Embarked": S  

Pentru umplerea celulelor goale, folosim `fillna()` si apoi salvam noul dataframe:

```
df[list_cols[i]] = df[list_cols[i]].fillna(mean_value)
# (...)
df.to_csv('../Date/task8_train')
```
