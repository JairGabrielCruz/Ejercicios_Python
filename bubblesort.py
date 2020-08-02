# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 16:02:46 2020

@author: HP
"""
def bubblesort(array):
    length=len(array)-1
    for i in range(0,length):
        for j in range(0,length):
            if array[j]>array[j+1]:
                aux=array[j]
                array[j]=array[j+1]
                array[j+1]=aux
    return array
ran=[(60,70,0,80,85,50)]:
print("Antes de ordenar:")
print(ran)
print("Despues de ordenar:")
print(bubblesort(ran)) 
        

