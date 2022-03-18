nombre = "Alan"
curso = "Youtube"
result = "{} esta tomando un curso en {}".format(nombre, curso)
print(result)
result = "{a} toma un curso en {b}".format(b = curso, a = nombre)
print(result)
# Todos los caracteres en minuscula
print(result.lower())
# todos los caracteres en mayusculas
print(result.upper())
# cada primer caracteres en mayuscula
print(result.title())
# Encontrar la posicion en la que comienza una palabra
print(result.find("curso"))
# encontrar la pocision en que que comienza a usarse la variable
print(result.find(curso))
# contar la cantidad de veces que se repite un caracter
print(result.count("u"))
# remplazar todos un caracter
print(result.replace('u', 'x'))
# dividir/cortar los datos de un un string devolviendo una lista
# Corta cada ves que encuentre un 'espacio', puede ser cualquier cosa
print(result.split(" "))
print(result.split("u"))