# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 19:38:49 2025

@author: corte
"""

def Num_Perf():
  primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  num_perfectos = []

  for p in primos:
    formula = (2**p) - 1

    perfect_number = (2**(p-1)) * formula
    num_perfectos.append(perfect_number)
  return num_perfectos
print(Num_Perf())

# %%

def Num_mersenne():
  primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  num_mersenne = []

  for p in primos:
    mersenne_candidate = (2**p) - 1
    num_mersenne.append(mersenne_candidate)
  return num_mersenne
print(Num_mersenne())

# %%
def Num_Fermat():
  valores = [0, 1, 2, 3, 4]
  num_fermat = []

  for n in valores:
    numerosfermat = (2**(2**n)) + 1

    num_fermat.append(numerosfermat)
  return num_fermat

print(Num_Fermat())

# %%
import random as rd

def Num_Euler():
  primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  num_euler = []
  a = rd.randint(1, 5)
  for p in primos:
    solucion = p**(a) - p**(a-1)
    num_euler.append(solucion)
  return num_euler

print(Num_Euler())