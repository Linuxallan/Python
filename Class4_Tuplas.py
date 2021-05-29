# Tuplas a diferencias de las listas, no son modificables
# cuando se crea no se le puede agregar no borrar nada

from typing import Tuple


tupla = ("datos1", 56, "info_4")
print(tupla)
print(tupla[2])

# conevrtir tupla a lista
lista1 = list(tupla)
print(lista1[:])

# convertir de lista a tupla
tupla_1 = tuple(lista1)
print(tupla_1)

# buscar en tupla por dato
print("jjuan" in tupla_1)
print(56 in tupla_1)

# ver el largo de la tupla
print(len(tupla_1))

# copiar los valores de la tupla a variables (desempaquetar)
# NOTA : la cantidad de variables debe ser igual a la candidad de datos en 
# la tabla, si no manda error
dato1, num, masInfo = tupla_1
print(dato1)
print(masInfo)
print(num)

# copiar toda la tupla a una variable
hhh = tupla_1
print(hhh)