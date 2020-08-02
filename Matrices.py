# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:14:33 2020

@author: HP
"""
from random import randint
filas=int()
columnas=int()
datos=int()
print("Ingrese cuantas filas se requieren")
filas=int(input())
print("Ingrese cuantas columnas se requieren")
columnas=int(input())
matrix=[[int() for ind0 in range(columnas)] for ind1 in range(filas)]
for f in range(filas):
    for c in range(columnas):
        matrix[f-1][c-1]=randint(0,100)
for i in range(filas):
    print("|",end="")
    for j in range(columnas):
        print(matrix[i-1][j-1],"|",end="")
    print(" ")
print(" ")
print("El valor de la diagonal principal")
print(" ")
for i in range(filas):
    print("|",end="")
    for j in range(columnas):
        if i==j:
            print(matrix[i-1][j-1],"|",end="")
        else:
            print("-|",end="")
    print(" ")
print(" ")
print("El valor de la diagonal secundaria de la matriz es:")
print(" ")
for i in range(filas):
    print("|",end="")
    for j in range(columnas):
        if i+j==(filas-1):
            print(matrix[i-1][j-1],"|",end="")
        else:
            print("-|",end="")
    print(" ")