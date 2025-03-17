
#-----------------------------------Bibliotecas--------------------------------------------------------------#


import  pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------Carregar Arquivo CSV em um DataFrame-----------------------------------#

df=pd.read_csv("C:\Projetos\Heart_attack_risck_predicition\myenv\Dataset\heart-attack-risk-prediction-dataset.csv")

df['teste']=df['Age']*5

x=df['Age']
y= df['Heart rate']



import matplotlib.pyplot as plt


# Criando o gráfico
plt.bar(x, y, color='ciano')

# Adicionando rótulos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico Simples')

# Exibir o gráfico
plt.show()

#test