# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 15:24:42 2020

@author: HP
"""
def cantidad_dias(mes):
    if mes.lower()in("1","3","7","8","9","12"):
       return 31
    elif mes.lower()in("2"):
       return 28 
    else:
       return 30 

nombre_mes=input("Ingrese el nombre del mes:")
print(cantidad_dias(nombre_mes))

