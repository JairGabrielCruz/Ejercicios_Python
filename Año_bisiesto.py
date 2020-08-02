# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:33:52 2020

@author: Jair Cruz
"""

def es_bisiesto(año):
    if año %400==0:
        return True
    elif año %100==0:
        return False
    elif año %4==0:
        return True
    else:
        return False

año=2020
print(( es_bisiesto(año)))

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = es_bisiesto(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")




