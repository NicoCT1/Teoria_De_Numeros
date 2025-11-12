# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 19:38:02 2025

@author: corte
"""

import random

ternas_pitagoricas = {}
contador = 1

numeros = list(range(1, 31))

random.shuffle(numeros)

for a in numeros:
    for b in numeros:
        for c in numeros:
            if a**2 + b**2 == c**2:
                ternas_pitagoricas[f"Terna {contador}"] = {"a": a, "b": b, "c": c}
                contador += 1

print(ternas_pitagoricas)