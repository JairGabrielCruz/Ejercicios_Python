# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 16:10:00 2020

@author: HP
"""


def es_bisiesto(año):
    if año %4==0:
        return False
    elif año% 100==0:
        return True
    elif año%400==0:
        return False
    else:
        return True

def cantidad_de_dias(mes,año):
    return monthrange (año,mes)[1]

def dia_año(año,mes,dia):
    dias=0
    for m in range(1,mes):
        md=cantidad_de_dias(año, m)
        if md==None:
            return None
        dias+=md
    m=cantidad_de_dias(año, mes)
    if dia >=1 and dia <=md:
       return dias+dia
    else:      
        return None
    
print(dia_año(2020, 10, 9))