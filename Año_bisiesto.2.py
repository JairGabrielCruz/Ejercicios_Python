# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 00:10:06 2020

@author: HP
"""
def cantidad_dias(año,mes):
    bisiesto=False
    if año % 400 ==0:
        bisiesto=True
        
    elif año % 4 ==0:
        bisiesto = True
        
    if mes in (1,3,5,7,8,10,12):
        dias = 31
    elif mes == 2:
        if bisiesto:
            dias = 29
        else:
            dias = 28
    else:
        dias = 30
        return(año,mes)
print(cantidad_dias(2020, 2,))

