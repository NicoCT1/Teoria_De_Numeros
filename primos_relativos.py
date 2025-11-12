# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 19:35:50 2025

@author: corte
"""

def encontrar_mcd(a, b):

  while b:
    a, b = b, a % b
  return a

numero1 = 48
numero2 = 18
mcd = encontrar_mcd(numero1, numero2)
print(f"El MCD de {numero1} y {numero2} es: {mcd}")

if mcd == 1:
  print(f"{numero1} y {numero2} son primos relativos.")
else:
  print(f"{numero1} y {numero2} no son primos relativos.")

print("-" * 20) # Separador para el siguiente ejemplo

numero1 = 100
numero2 = 203
mcd = encontrar_mcd(numero1, numero2)
print(f"El MCD de {numero1} y {numero2} es: {mcd}")

if mcd == 1:
  print(f"{numero1} y {numero2} son primos relativos.")
else:
  print(f"{numero1} y {numero2} no son primos relativos.")