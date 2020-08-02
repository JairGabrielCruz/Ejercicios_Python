# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 13:07:15 2020

@author: HP
"""
temperatura = []
n = int(input("Ingrese la cantidad (1,10): "))
for i in range(n):
 num = int(input("Ingrese temperatura en °C :"))
 temperatura.append(num)
gas = 0
liquid = 0
solid = 0
for num in temperatura:
    if (num==100 or num>100):
        gass=gas+1
    elif (num < 0 or num==0):
        solid=solid+1
    elif (num>0 or num<100):
        liquid=liquid+1
print()
print("!RESUMEN DEL ANÁLISIS DE MUESTRAS DE AGUA!")
print("CANTIDAD DE MUESTRAS SÓLIDAS:", solid)
print("CANTIDAD DE MUESTRAS LÍQUIDAS:", liquid)
print("CANTIDAD DE MUESTRAS GASEOSAS:", gas)
i=0
print("REINGRESE EL VALOR DE LAS TEMPERATURAS")
tempo1=int(input("Temperatura 1 en °C:"))
tempo2=int(input("Temperatura 2 en °C:"))
tempo3=int(input("Temperatura 3 en °C:"))
tempoT =(tempo1+tempo2+tempo3)
centi =tempoT/3
f1 =(tempo1 * 9/5)+32
f2 =(tempo2 * 9/5)+32
f3 =(tempo3 * 9/5)+32
faren = (f1 + f2 + f3) / 3
print("TEMPERATURA PROMEDIO EN °C:", centi)
print("TEMPERATURA PROMEDIO EN °F:", faren)

