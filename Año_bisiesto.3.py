# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 23:35:15 2020

@author: Jair Cruz
"""
def es_bisiesto(año):
    if año%4==0:
        return False
    elif año% 100==0:
        return True
    elif año%400==0:
        return False
    else:
        return True

def cantidad_de_dias(año,mes):
     if año < 1900 or mes < 1 or mes > 12:
         return   
     dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
     res  = dias[mes -1]
     if mes == 2 and es_bisiesto(año):
	     res = 29
     return res


def dia_del_año(año , mes, dia):
    dias=0
    for m in range(1,mes):
        md = cantidad_de_dias(año, m)
        if md == None:
            return None
        
        dias += md
        
    md = cantidad_de_dias(año , mes)
    if dia >= 1 and dia <= md:
        return dias + dia
    else:
        return None   
print(dia_del_año(2020,12,31)) 

