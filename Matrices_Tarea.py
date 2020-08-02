# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 06:59:37 2020

@author: Jair Gabriel Cruz
"""
import numpy as np
from random import randint
print("Ingrese el numero de filas")
fi=int(input())    
print("Ingrese el numero de columnas")
colum=int(input())
print("\n"*0)
matriz=np.zeros([fi,colum])
fl=-1
co=-1
g=fi
p=fi
for i in range(0,fi):
    for n in range(0,colum):
        matriz[i][n]=int(randint(0,99))
print("La matriz es",fi,"x",colum)
print("\n"*0)
print(matriz)
print("\n"*0)
print('Diagonal principal')
print("\n"*0)
for j in range(0,fi):
    if fl<fi:
        fl+=1
        g-=1
    print(' ||'*fl,"|",int(matriz[j][fl]),"|",'|| '*g)
    
print('Diagonal Secundaria')
print("\n"*0)
for k in range(0,fi):
    if co<fi:
        co+=1
        p-=1
    print(' ||'*p,"|",int(matriz[k][p]),"|",'|| '*co)


