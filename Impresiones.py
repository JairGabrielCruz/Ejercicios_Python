# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:52:05 2020

@author: Jair Gabriel Cruz
"""

if __name__ == '__main__':
	contadori = int()
	final = int()
	n = int()
	total = int()
	BN = float()
	color = float()
	BN = 0.06
	color = 0.12
	total = 0
	while True:
		print("Ingrese contador inicial")
		inicial = int(input())
		if inicial>0: break
	while True:
		print("Ingrese contador final")
		final = int(input())
		if (final<=inicial):
			print("Error, Ingrese nuevamente una nueva cantidad")
		if final>=inicial: break
	while True:
		print("Elija la impresora 1 para B/N y 2 para Color")
		n = int(input())
		if (n>1 or n<2) and n>0: break
	total = final-inicial
	print("Impresiones = ",total)
	if (n==1):
		print("Costo= $ ",total*BN)
	else:
		print("Costo= $ ",total*color)