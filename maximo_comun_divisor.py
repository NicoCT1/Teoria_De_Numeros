# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 19:32:40 2025

@author: corte
"""

mcd1 = int(input("Ingrese el primer número: "))
mcd2 = int(input("Ingrese el segundo número: "))

print(f"Los números ingresados son: {mcd1} y {mcd2}")

num1 = mcd1
num2 = mcd2


while mcd2 != 0:
    resto = mcd1 % mcd2
    print(f"Calculando: {mcd1} % {mcd2} = {resto}")

    mcd1 = mcd2
    mcd2 = resto

print(f"El máximo común divisor (MCD) de {num1} y {num2} es: {mcd1}")


