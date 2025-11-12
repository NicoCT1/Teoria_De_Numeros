# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 19:34:53 2025

@author: corte
"""

mcd1 = int(input("Ingrese el primer número: "))
mcd2 = int(input("Ingrese el segundo número: "))

print(f"Los números ingresados son: {mcd1} y {mcd2}")

num1 = mcd1
num2 = mcd2
multiplicadores = []

while mcd2 != 0:
    resto = mcd1 % mcd2
    print(f"Calculando: {mcd1} % {mcd2} = {resto}")

    contador = 1
    while True:
        if mcd2 * contador + resto == mcd1:
            print(f"El multiplicador es: {contador}")
            multiplicadores.append(contador)
            break
        else:
            contador += 1

    mcd1 = mcd2
    mcd2 = resto

print(f"El máximo común divisor (MCD) de {num1} y {num2} es: {mcd1}")
print(f"Lista de multiplicadores encontrados: {multiplicadores}")

for i, multiplicador in enumerate(multiplicadores, start=1):
    print(f"q{i} = {multiplicador}")