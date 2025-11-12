# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 19:27:39 2025

@author: cortes
"""

def hexadecimal(a):
    digitos = "0123456789ABCDEF"
    resultado = []
    numero = a
    if numero == 0:
        return "0"

    if numero < 0:
        numero = abs(numero)

    while numero > 0:
        residuo = numero % 16
        resultado.append(digitos[residuo])
        numero //= 16

    resultado.reverse()
    return "".join(resultado)

num = int(input("Ingresa un número decimal: "))
print(f"El número en hexadecimal es: {hexadecimal(num)}")