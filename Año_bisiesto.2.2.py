# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:59:09 2020

@author: Jair Cruz
"""


from calendar import monthrange
try:
    def cantidad_de_dias(mes,año):
        return monthrange (año,mes)[1]
    print(cantidad_de_dias(12,2000))
except:
    print("El valor ingresado es incorrecto, ingrese otro valor")

