# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:56:10 2020

@author: Jair Gabriel Cruz
"""
#Calificacion total del estudiante 
calificacion_1=int(input("Ingrese la calificacion de su primera evaluacion:"))
calificacion_2=int(input("Ingrese la calificacion de su segunda evaluacion:"))
calificacion_3=int(input("Ingrese la calificacion de su tercera evaluacion:"))
if calificacion_1>=calificacion_3 and calificacion_2>=calificacion_3:
    calificacion_final=calificacion_1+calificacion_2
else:
    if calificacion_1>=calificacion_2 and calificacion_3>=calificacion_2:
        calificacion_final=calificacion_1+calificacion_3
    else:
        calificacion_final=calificacion_2+calificacion_3
print("Su calificación total es:",calificacion_final)

