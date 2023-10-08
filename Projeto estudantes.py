import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt 
import os

import warnings 
warnings.filterwarnings ('ignore')

os.chdir('C:\\Users\\andre\\OneDrive\\Área de Trabalho\\python\\Projeto Estudantes')

#lendo a Base de Dados 
Base_Dados = pd.read_csv('StudentsPerformance.csv')

#dimensão 
print(Base_Dados.shape)

#Head
print(Base_Dados.head())

#Campos nulos 
Nulos = Base_Dados.isnull()

plt.figure(figsize=(16,5))
plt.title('Analise de campos nulos')
sns.heatmap(Nulos, cbar=False);
plt.show()

# Campos Unicos
print(Base_Dados.nunique())

# Campos Duplicados 
print('Estes são os campos duplicados: ',Base_Dados.duplicated().sum())

# Estatisticas de % 
print(Base_Dados.describe())

#Info
print(Base_Dados.info())

print(Base_Dados['gender'].value_counts(normalize=True)*100)

print(Base_Dados['race/ethnicity'].value_counts(normalize=True)*100)

print(Base_Dados['parental level of education'].value_counts(normalize=True)*100)

print(Base_Dados['lunch'].value_counts(normalize=True)*100)

print(Base_Dados['test preparation course'].value_counts(normalize=True)*100)

# Graficos
sns.boxplot(data=Base_Dados, x='math score', y='gender')
plt.show()

sns.boxplot(data=Base_Dados, x='reading score', y='gender')
plt.show()

# Grafico
sns.boxplot(data=Base_Dados, x='writing score', y='gender')
plt.show()

Base_Dados.groupby(by= ['gender']).describe()['math score'].reset_index()

#Grafico
sns.pairplot(Base_Dados, hue='race/ethnicity')
plt.show()

sns.boxplot(data=Base_Dados, x='math score', y='race/ethnicity')
plt.show()

sns.boxplot(data=Base_Dados, x='math score', y='parental level of education')
plt.show()

Base_Dados.groupby(by=['parental level of education']).describe()['math score'].reset_index()

sns.boxplot(data=Base_Dados, x='math score', y='test preparation course')
plt.show()

Base_Dados.groupby(by=['test preparation course']).describe()['math score'].reset_index()

sns.scatterplot(data=Base_Dados, x='math score', y='writing score')
plt.show()