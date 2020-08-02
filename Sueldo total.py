# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:37:28 2020

@author: Jair Gabriel Cruz
"""
#Total a pagar al obrero 
horas=int(input("Ingrese las horas trabajadas:"))
precio_horas=int(input("Ingrese el precio por cada hora trabajada:"))
descuento=int(input("Ingrese el descuento"))
print("\n")
if horas<=40:
    valor_total=horas*precio_horas-descuento
else:
    valor_total=40*precio_horas+1.5*precio_horas*(horas-40)-descuento
print("El valor a pagar al obrero es",valor_total)
