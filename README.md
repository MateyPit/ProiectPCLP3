# Proiect PCLP3

#### NICOLESCU Petre - 314CD

Acest proiect are ca obiectiv prelucrarea setului de date "Titanic", care contine o varietate 
de informatii despre pasagerii Titanicului, precum numele, varsta, tariful platit, numarul de
rude, etc. Scopul final este obtinerea unor statistici care au potentialul de a prezice sansa
de supravietuire a unui individ de pe nava Titanic. In Partea I, ne vom axa pe calcularea acestor
procentaje, vom studia modul in care diferitele caracteristici ale pasagerilor afecteaza aceste
rezultate si vom incerca sa tragem cateva concluzii pe tiparelor identificate.

Primul pas este stocarea datelor din fisierul oferit drept suport, 'train.csv', prin intermediul
unui *Dataframe Pandas*:
```
df = pd.read_csv('train.csv')
```

## Cerinta 1



![This is a graph!](/ParteaI/Task3_AgeHistogram.png "Age Histogram")
