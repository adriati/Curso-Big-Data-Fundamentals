'''
Created on 1 ago. 2018

@author: adriati
'''
import numpy as np
import pandas as pd
import random
import csv
import math


def puntos_iniciales (num, tam):
    vector = np.zeros(num, dtype = int)
    for i in (range(num)):
        vector[i] = int(random.randrange(tam))
    return vector

def asigna_cluster (x, centros):
    cercano = 0
    distancia = 99999
    
    for i in range(len(centros)):
        tmp = 0  
        y = centros.iloc[i]
        
        for j in (range(len(x))):
            tmp = tmp + (float(x[j]) - float(y[j]))*(float(x[j]) - float(y[j]))
        tmp = math.sqrt(tmp)
        
        if (tmp < distancia):
            distancia = tmp
            cercano = i
    
    return cercano

#tam = numero de clusters
def calcula_centros (puntos, clusters, tam):
    centros = np.zeros(tam*2, dtype = float).reshape((tam,2))
    for i in range(tam):
        tmp = puntos[clusters == i]
        centros[i] = tmp.sum(axis = "rows")/len(tmp)
        
    return centros     

#Cargamos los puntos
puntos = []
with open('Test-case-3.txt', newline='') as inputfile:
    cabecera = inputfile.readline()
    for row in csv.reader(inputfile, delimiter = "\t"):
        puntos.append(row)

tam = cabecera [0:3]
tam = int(tam)
puntos= pd.DataFrame(puntos, dtype = float)        
centros = puntos_iniciales(tam, len(puntos))
centros = puntos.iloc[centros]


#Asignamos CLusters
cluster = np.zeros(len(puntos), dtype = int)
iter = 0

while(True):  
    for i in range(len(puntos)):
        tmp = asigna_cluster (puntos.iloc[i], centros)
        cluster[i] = tmp

    nuevos_centros = calcula_centros(puntos, cluster, tam)
    
    if(np.array_equal(nuevos_centros ,centros)):
        break
    else:
        iter += 1
        centros = nuevos_centros
        centros = pd.DataFrame(centros)

print (centros)        

puntos_cluster = np.zeros(tam, dtype = int)
for i in range(tam):
    puntos_cluster[i] = len(puntos[cluster == i])
    print("Puntos en Cluster ",  i + 1, " ", puntos_cluster[i])
    
print("Numero de iteraciones ", iter)
