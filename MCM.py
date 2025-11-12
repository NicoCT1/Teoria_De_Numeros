# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 19:30:59 2025

@author: cortes
"""

a = int(input("Ingrese la cantidad de números a los que les quiere sacar el MCM: "))

resultado = int(input("Ingrese el número: "))

for i in range(a - 1):
    num = int(input("Ingrese el número: "))

    x, y = resultado, num
    while y != 0:
        x, y = y, x % y
    mcd = x

    resultado = abs(resultado * num) // mcd

print("El MCM de los números ingresados es:", resultado)