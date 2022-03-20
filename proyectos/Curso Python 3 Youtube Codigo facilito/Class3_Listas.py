# 'Listas' -> y al final es 'Diccionarios'

lista1 = ["alien", "diego", "Juan"]
# ' : ' es para escribir todos los elementos de mi lista
print(lista1[:])
# para acceder a una ubicacion concreta se debe escribir el numero
# que hace referencia a la posicio, estas listas comienzan en 0
print(lista1[1])
# Python le da la vuelta a los numeros negati vos, los transforma apositivos
# pero ademas comienza a recorrer la lista de derecha a izquierda
# comenzando con el ultimo valor en -1
print(lista1[-1])

# imprimir multitud de valores concretos
print(lista1[0:2])

# agregar elementos a la lista 'append'
lista2 = []
lista2.append("archivo1")
lista2.append(34)
print(lista2[:])

# agregar mas de 1 elemento a la lista 'extend'
# se agregan desde el final
lista2.extend(["extencion1", "ext_2"])
print(lista2[:])

# sumar listas (concatenar) 
lista_3 = lista1 + lista2
print("Concatenando listas ", lista_3[:])

# insertar un dato entremedio de la lista (en este caso en la posicion 1)
lista2.insert(1,"wordInsertado")
print(lista2[:])

# buscar el indice de un dato
print(lista2.index("wordInsertado"))

# ver si un elemento se encuentra en la lista
# es boolean, devuelve true si se encuentra, y false si no
print("Pepe" in lista2)
print("ext_2" in lista2)

# eliminar un dato por su contenido 'remove'
lista2.remove("extencion1") #str
lista2.remove(34)           #int
print(lista2[:])

# eliminar el ultimo dato de la lista 'pop'
lista2.pop()
print(lista2[:])

# ver el largo de la lista
print(len(lista2))

###
###
# Diccionarios ; solo puede existir una clave, pero los datos se pueden 
# repetir
diccionario_1 = {"claveIndice" : "valor", "gmail" : "password", 45 : "numeros", "masNum" : 776}
print(diccionario_1)
# agregar un dato con su clave a el diccionario
diccionario_1["Italia"] = "Roma"
print(diccionario_1)
# eliminar una tupla del diccionario
del diccionario_1["gmail"]
print(diccionario_1)
# mostrar las claves del diccionario
print(diccionario_1.keys())
# imprimir valores del diccionario
print(diccionario_1.values())
# largo del diccionario
print(len(diccionario_1))
