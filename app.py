
#-----------------------------------Bibliotecas--------------------------------------------------------------#


import  pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------Carregar Arquivo CSV em um DataFrame-----------------------------------#

df=pd.read_csv("C:\Projetos\Heart_attack_risck_predicition\myenv\Dataset\heart-attack-risk-prediction-dataset.csv")

print('Dataset loaded.')
print('Shape:', df.shape)
print('Columns:', df.columns.tolist())

# # Criando o gráfico
# plt.plot(x, y, color='red')

# # Adicionando rótulos
# plt.xlabel('Eixo X')
# plt.ylabel('Eixo Y')
# plt.title('Gráfico Simples')

# # Exibir o gráfico
# plt.show()

#testssss