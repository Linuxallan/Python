valid = False

# Condicional IF 1
if valid :
    print("Es {}".format(True))
else:
    print("Es {}".format(False))

valid = True

# Condicional IF 2
mensaje = "Es {}".format(True) if valid else "Es {}".format(False)
print(mensaje)

# pass para no construir retorno
product = "Gorro"

if product == "Pera":
    print("Es fruta: %s" %(product))
elif product == 1:
    pass
else:
    print("El %s no es una fruta" %(product))

list = []
if list:
    print("contiene datos")
else:
    print("esta vasia")

## ------ While Cycle

number = 34
while number < 40 :
    print(number)
    number+=1
else:
    print("Numero es 40 o mayor")

number = 1
while number < 10 :

    print(number)
    number+=1

    if number == 5:
        continue

    if number == 7:
        break
    
else:
    print("Numero es 40 o mayor")


#---------- For

list = [1,1,2,2,12,1,12,21,1,221,32,32,23]
for valor in list:
    print(valor)

for valor in range(len(list)):
    print(valor)

for valor in range(10,18):
    print(valor)

# recorrer lista retornando indice y valor -> Method: 'enumerate()'
for index, valor in enumerate(list):
    print("El indice del valor {} es: {}".format(valor, index))

# EJEMPLO en JAVA o C#
# for(int i = 0 ; i < list.lenght ; i++){
for valor in range(0, len(list)):
    print(valor)

# For para diccionarios
diccionario = {'a': 10, 'c': 23, "s4": True}
for key, value in diccionario.items():
    print("La claves %s tiene el valor de %s" %(key, value))


## --------- Crear listas con cyclos
# list Comprehension 
lista = [ valor for valor in range(0,101)]
print(lista)

# solo valores pares
lista = [ valor for valor in range(0,101) if valor%2 == 0 ]
print(lista)

# Mas list converhension en tuplas y diccionarios
# https://www.youtube.com/watch?v=Z-8Khdd2BUQ&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM&index=15
