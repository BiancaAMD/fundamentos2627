'''
1. FUNCIONES: 
-ESTRUCTURA

def area_rectangulo(base: float, altura: float) -> float:
    
    return base * altura
    
print(area_rectangulo)

-DEVOLVER VARIOS VALORES

def area_y_perimetro(base: float, altura: float) -> (float, float, float):
    return base * altura, 2 * (base + altura), base*base

area, perimetro, doble_base = area_y_perimetro(4, 3)
print(f"El área es {area} y su perímetro es {perimetro}") 
print(f"El doble de su base es: {doble_base}")



2. PARÁMETROS:

-POSICIONALES Y POR NOMBRE

def presentar(nombre: str, edad: int) -> str:
    return f"{nombre} tiene {edad} años"

print(presentar("Ada", 36))              # por posición
print(presentar(edad=36, nombre="Ada"))  # por nombre: el orden da igual


-PARÁMETROS POR DEFECTO

def precio_con_iva(precio: float, iva: int = 21) -> float:
    return precio * (1 + iva / 100)

print(precio_con_iva(100))        # 121.0  (usa el 21 que habíamos establecido)
print(precio_con_iva(100, 10))    # 110.0  (usa el 10)



3. ÁMBITO DE LAS VARIABLES:

total = 0 #variable GLOBAL
def calcular() -> int:
    total = 10        # variable LOCAL
    return total

total = calcular()

print(total)   
       
# ✗ NameError: 'total' no existe fuera, en el caso de:
#- no hayamos creado una variable global
#- asignado total = calcular() por ej


4. LISTAS

notas: list[float] = [5.0, 7.5, 9.0, 4.5]

print(notas[0])        # 5.0    primer elemento (se empieza en 0)
print(notas[-1])       # 4.5    último
print(len(notas))      # 4      cuántos hay

- Operaciones básicas: 

notas.append(6.0)      # añadir al final
print(sum(notas))      # 32.0   suma de todos
print(max(notas))      # 9.0    el mayor
print(min(notas))      # 4.5    el menor

- Funciones con listas

def media(numeros: list[float]) -> float:
    return sum(numeros) / len(numeros)


print(media([5.0, 7.5, 9.0]))      # 7.166666666666667


5. LIBRERÍAS

- Importar:
import math
print (math.acos(0.5))

import statistics
notas: list[float] = [5.0, 7.5, 9.0, 4.5]
print(statistics.mean(notas)) #enseña la media de las notas

print(math.pi)


from math import sqrt
print(sqrt(4)) 


from statistics import mean
notas: list[float] = [5.0, 7.5, 9.0, 4.5]
print(mean(notas)) 


import random
print(random.randint(1,6))

-Tres librerías útiles:

    import random
    notas: list[float] = [5.0, 7.5, 9.0, 4.5]
    vocales : list[str] = ["a", "e", "i", "o", "u"]

    print(random.rand(1, 6))        # número al azar entre 1 y 6
    print(random.choice(vocales))  # elemento al azar de una lista

    import statistics
    print(statistics.mean([2, 4, 6]))     # 4      media
    print(statistics.median([1, 5, 9]))   # 5      mediana




'''




