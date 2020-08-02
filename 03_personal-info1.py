# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:44:26 2020

@author: HP
"""


nombre=input("Ingrese su nombre:")
apellido=input("Ingrese su apellido:")
edad=int(input("Ingrese su edad:"))
if edad >=0 and edad<=10:
    print("Usted es un niño/a")
elif edad >=11 and edad <=17:
    print("Usted es un adolescente")
elif edad >=18 and edad <=40:
    print("Usted es joven")
elif edad >=41 and edad <=62:
    print("Usted es un adulto")
elif edad >=63 and edad <=80:
    print("Usted es un adulto mayor")
else:
    print ("Usted es un adulto")
ubicación=input("Ingrese su ubicación:")

space= int(print("Su nombre es"+nombre,apellido+"usted tiene"+edad+"años"+"y vive en la ciudadela"+ubicación))

           
 