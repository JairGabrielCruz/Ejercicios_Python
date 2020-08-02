# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:52:46 2020

@author: Jair Gabriel Cruz
"""
#Compra total de las llantas 
cantidad=int(input("Ingrese la cantidad de llantas:"))
precio_individual= int(input("Ingrese el precio unitario de cada llanta:"))
if cantidad>4:
    precio_total=0.9*precio_individual
total_compra=cantidad*precio_individual
print("\n")
print("El total de su compra es:",total_compra)


