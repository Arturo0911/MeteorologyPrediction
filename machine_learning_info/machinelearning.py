# -*- coding: utf-8 -*-
"""machineLearning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GfXYszW8cUpxjEion33897kSR5KjgR7o
"""

import torch
import numpy as np
import pandas as pd

"""```
# This is formatted as code
```
[*] Trabajando con adornos
"""

torch.__version__

tensor_a = torch.ones(2,2) # aqui imprimimos tensores de dimension 2x2 así como se 
# coloca
tensor_a

tensor_b = torch.Tensor(2,2)
tensor_b

"""el tensor (tensor_b = torch.Tensor(2,2))
Me devuelve valores aleatorios
"""

tensor_b.uniform_(0,1)

"""Cuando usamos el método uniform_(value, another_value)
estos me devuelven valores aleatorios entre esos números
"""

tensor_c = torch.rand(2,2)
tensor_c

"""#ahora sumaremos tensores
'''
tensor([[0.3242, 0.2531],
        [1.0777, 0.1175]])
'''
tensor_result = tensor_b + tensor_c
tensor_result
"""

# con esto podemos dibujar la forma y el tamaño del tensor
tensor_result = tensor_b -tensor_c
tensor_result.shape

reshaped = tensor_result.view(1,4)
# Ahora pasamos de tenere una matriz de 2x2 como se mostraba ahí a tener un solo arrgeglo de 1x4 (una fila, 4 elementos)
# tensor([[0.3242, 0.2531, 1.0777, 0.1175]])
reshaped

# ahora especificaremos el valor del tensor
points = torch.tensor([[1.0,2.0],[7.0,25.0]])
points

# SI QUIERO cambiar el direccionamiento de algun valor 
# cambiamos como si fuera una matriz

print(points[0][1])
points[0][1] = 3.27
points

# para verificar como se está almacenado
# usamos el método storage()
points.storage()

# para saber como puede pasar de un elemento a otro
# usamos el método stride()

points.stride()

p_t = points.t()
p_t

# agregar dimensiones

tensor_x  = torch.tensor([1,2,3,4])
print(tensor_x)
torch.unsqueeze(tensor_x, 1)

"""Representar datos en nuestros sensores"""

numpyArray = np.random.randn(2,2)
from_numpy = torch.from_numpy(numpyArray)
from_numpy

"""Tensores clase 6"""

# vamos a sacar la media
print("la matriz original: ",from_numpy)
torch.mean(from_numpy)
print("quiero imprimir la dimension 0: ", torch.mean(from_numpy, dim=0))
print("quiero imprimir la dimension 1: ", torch.mean(from_numpy, dim=1))

# para desviación estándar es std

torch.std(from_numpy, dim= 1)

torch.save(from_numpy, 'tensor.t')

load = torch.load('tensor.t')
load

# use dataframes
url = "https://raw.githubusercontent.com/amanthedorkknight/fifa18-all-player-statistics/master/2019/data.csv"
dataframe = pd.read_csv(url)
dataframe



# nombre de columnas
dataframe.columns

"""
subset = dataframe[['Overall','Age','International Reputation', 'Weak Foot',
       'Skill Moves']] este es el original, pero se modificó porque 

       cuando sacábamos el promedio 'mean' lanzaba valores nan 
       y esto porque de las columnas que agarré había algunas que 
       no tenían reputación internacional
"""
subset = dataframe[['Overall','Age','International Reputation', 'Weak Foot',
       'Skill Moves']].dropna(axis=0, how ='any')
subset

columns = subset.columns[1:]
players = torch.tensor(subset.values).float()
players.shape, players.type()

# la columna de overall no la quiero por eso 1: colocamos
data = players[:, 1:]
data, data.shape

# solo la primera columna es decir el overall
target = players[:, 0]
target, target.shape

# aqui estoy definiendo el dataset para verificar que solo tome del primer valor [:, 0]
print(players[:,0])
# aqui muestra la segunda columna. 
print(players[:,1])
print(players)

# el promedio 
mean = torch.mean(data, dim=0)
mean

# la desviacion estándar
std = torch.std(data, dim=0)
std

#normalizar

norm = (data-mean)/torch.sqrt(std)
norm

# vamos a dividir a los jugadores mejores
# usamos la funcion ge (greater or equal)
# como segundo argumento los que tienen más de 85
# en average colocamos dos funciones torch que
# serian  lt (lesser than)
good = data[torch.ge(target, 85)]
average = data[torch.gt(target, 70) & torch.lt(target, 80)]
not_so_good = data[torch.lt(target, 70)]

good_mean = torch.mean(good, dim=0)
average_mean = torch.mean(average, dim=0)
not_good_mean = torch.mean(not_so_good, dim=0)

good_mean, average_mean, not_good_mean

# con esta funcion for, vamos a agruparlos de mejor manera
print(target)
print(data)

for i, args in enumerate(zip(columns, good_mean, average_mean, not_good_mean)):
  print('{:25} {:6.2f} {:6.2f} {:6.2f}'.format(*args))

target

data

players

columns