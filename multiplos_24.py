# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 19:36:50 2025

@author: corte
"""

def product():
    numeros = list(range(1, 101))
    for i in range(len(numeros) - 2):
        a, b, c = numeros[i], numeros[i+1], numeros[i+2]
        resultado = a * b * c

        print(f"{a} * {b} * {c} = {resultado}")

        if a % 2 == 0 and resultado % 24 == 0:
            print("→ El producto es múltiplo de 24")
        print()

product()