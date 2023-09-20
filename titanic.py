# -*- coding: utf-8 -*-
"""titanic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F75fCIGJS2vfjb0dEKiyjcM1AsrX7nqu
"""

from google.colab import files
files.upload()

!rm -r ~/.kaggle
!mkdir ~/.kaggle
!mv ./kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle competitions download -c titanic

! unzip '/content/titanic.zip'

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

df = pd.read_csv('/content/tested.csv')

df

"""# visulation

"""

df.isnull().sum()

df.shape

df.info()

df.describe()

plt.bar(df["Sex"], df["Survived"])
plt.title('survived gender')
plt.xlabel('sex')
plt.ylabel('Survived')
plt.show()

survived_female=df.loc[(df["Survived"]==0) & (df["Sex"]=="female")].value_counts()
survived_female

survived_female=df.loc[(df["Survived"]==1) & (df["Sex"]=="female")].value_counts()
survived_female

survived_male=df.loc[(df["Survived"]==0) & (df["Sex"]=="male")].value_counts()
survived_male

survived_male=df.loc[(df["Survived"]==1) & (df["Sex"]=="male")].value_counts()
survived_male

df['age_range'] = pd.cut(df['Age'], bins=[17, 27, 37, 47, 57, 67], labels=['17-27', '28-37', '38-47', '48-57', '58-67'])

age_range = df.groupby('age_range')['Age'].count()
age_range

df['age_range'].dtype

age_survived_female=df.loc[df["Survived"]==1]["age_range"]
age_survived_female

age_survived_female=age_survived_female.dropna()
age_survived_female

labels=['17-27', '28-37', '38-47', '48-57', '58-67']
plt.pie(age_range, labels = labels)
plt.title('Range of age')
plt.show()

Embarked_Q=df[(df["Embarked"]=="Q") & df["Survived"]==1].value_counts().count()

Embarked_S=df[(df["Embarked"]=="S") & df["Survived"]==1].value_counts().count()

Embarked_C=df[(df["Embarked"]=="C") & df["Survived"]==1].value_counts().count()

embarked=[Embarked_Q,Embarked_S,Embarked_C]
labels=['Q','S','C']
plt.pie(embarked, labels = labels)
plt.title('Survived Embarked')
plt.show()

pclass1=df[(df["Pclass"]==1) & df["Survived"]==1].value_counts().count()

pclass2=df[(df["Pclass"]==2) & df["Survived"]==1].value_counts().count()

pclass3=df[(df["Pclass"]==3) & df["Survived"]==1].value_counts().count()

survived=df[df["Survived"]==1].value_counts().count()

pclass=[pclass1,pclass2,pclass3]
labels=['1','2','3']
plt.bar(labels, pclass)
plt.title('survived pclass')
plt.xlabel('pclass')
plt.ylabel('Survived')
plt.show()

pclass1=df[(df["Pclass"]==1) & df["Survived"]==0].value_counts().count()

pclass2=df[(df["Pclass"]==2) & df["Survived"]==0].value_counts().count()

pclass3=df[(df["Pclass"]==3) & df["Survived"]==0].value_counts().count()

pclass=[pclass1,pclass2,pclass3]
labels=['1','2','3']
plt.bar(labels, pclass)
plt.title('unsurvived pclass')
plt.xlabel('pclass')
plt.ylabel('unSurvived')
plt.show()

correlation_matrix = df.corr().round(2)

sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.heatmap(data=correlation_matrix, annot=True)

df=df.dropna()

df

df['Embarked'] = df['Embarked'].astype('category')
df["Embarked"] = df["Embarked"].cat.codes

df['Sex'] = df['Sex'].astype('category')
df["Sex"] = df["Sex"].cat.codes

df['Pclass'] = df['Pclass'].astype('category')
df["Pclass"] = df["Pclass"].cat.codes

y = df['Survived']
x = df[['Embarked', 'Age','Sex','Pclass','Fare']]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=None)

model = linear_model.LogisticRegression().fit(x_train, y_train)

Y_pred = model.predict(x_train)
Y_pred

y_pred = model.predict(x_test)
y_pred

metrics.accuracy_score(y_train, Y_pred)

metrics.accuracy_score(y_test, y_pred)