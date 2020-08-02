# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:20:18 2020

@author: HP
"""
from random import randint
from time import sleep
preguntar=True
tempo = int()
caracter=str()
lista=[int()for ind3 in range(30)]
while preguntar:
    print("Para terminar la ejecución digite 0")
    print("Ingresar el tamaño del vector")
    tamaño_vector=int(input())
    if tamaño_vector>=3 and tamaño_vector<=30:
        while preguntar:  
            print("Digite 0 para cambiar el tamaño del vector")
            print("Si desea trabajar con carcatereses digite 1 y digite 2 para trabajar con numeros")
            pregunta=int(input())
            if pregunta==1 :
                for i in range(1,tamaño_vector+1):
                    print("Ingrese el nombre elegido",i)
                    caracter=input()
                    lista[i-1]=caracter
                    print("El valor en la posicion ",i," es  ", lista[i-1])
                for j in range(1,tamaño_vector+1):
                    for l in range(1,tamaño_vector):
                        if lista[l-1]>lista[l]:
                            tempo = lista[l-1]
                            lista[l-1]=lista[l]
                            lista[l]=tempo
                for k in range(1,tamaño_vector+1):
                    print("\n"*0)
                    print("El vector ordenado en la posicion ",k," es ",lista[k-1])
            elif pregunta==0:
                break
            else:
                for i in range(1,tamaño_vector+1):
                    lista[i-1]=randint(3,30)
                    print("\n"*0)
                    print("El valor en la posicion ",i," es  ", lista[i-1]) 
                    sleep(1)
                sleep(1)
                while preguntar:
                    print("Digite 0 para volver a escoger con que trabajar, si no es asi elija otra opción")
                    print("Para ordenar de menor a mayor digite 1 y digite 2 si es de mayor a menor digite")
                    pregu=int(input())
                    if pregu == 1:
                        for j in range(1,tamaño_vector+1):
                            for l in range(1,tamaño_vector):
                                if lista[l-1]>lista[l]:
                                    tempo = lista[l-1]
                                    lista[l-1]=lista[l]
                                    lista[l]=tempo
                        for k in range(1,tamaño_vector+1):
                            print("El vector ordenado en la posicion ",k," es ",lista[k-1])
                    elif pregu==0:
                        break
                    else:
                        for j in range(1,tamaño_vector+1):
                            for l in range(1,tamaño_vector):
                                if lista[l-1]<lista[l]:
                                    tempo = lista[l-1]
                                    lista[l-1]=lista[l]
                                    lista[l]=tempo
                        for k in range(1,tamaño_vector+1):
                            print("El vector ordenado en la posicion ",k," es ",lista[k-1])         
    elif tamaño_vector>30:
        print("El numero que ingreso excede el limite de 30, ingrese otro número menor")
    elif tamaño_vector== 0:
        preguntar = False
    else:
        print("El numero que ingreso no alcanza el limite de 3, ingrese otro número mayor")




