# Las Tuplas son inmutables
tuple_one = (45, "fer", False)
print(tuple_one)
print(tuple_one[1])

# Lista  (Si se modifica)
list_one = []
# Tuple  (No se modifica)
tuple_one = ()

#------- Diccionarios
# los diccionarios no usan indices, sino : clave , valor
dictionary_one = {'a':34, "Alan": True, 'a':"remplazo valor"}
print(dictionary_one)
# Las claves son inmutables
# Los valores si se pueden modificar

# agregar nuevo dato al diccionario
dictionary_one['c3'] = "nuevo dato"
dictionary_one["Alan"] = False
print(dictionary_one)

# buscar y retorar el valor de la clave especifica
# El primer parametro es la clave a buscar, el segundo es lo que retorna si la clave no existe
search = dictionary_one.get('z', "No existe la clave")
print(search)

# Eliminar clave/valor del diccionario
del dictionary_one["Alan"]
print(dictionary_one)

# Traer claves
print(dictionary_one.keys())
# convertir a una lista el retorno
print(list(dictionary_one.keys()))
# traer valores
print(dictionary_one.values())
# convertir a una tupla el retorno
print(tuple(dictionary_one.values()))

# Agregar datos al diccionario
#print(dictionary_one.update('r4' = 34, "ggg" = 455))