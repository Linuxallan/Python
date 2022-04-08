import json 

lista_datos = []

y = 1
while y <= 7000:
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    print("Ingrese numero")
    num = input()
    lista_datos.append(num)


lista_json = []
largo = len(lista_datos)//7

cont = 0
for valor in range(largo):

    cadena = ""
    for value in range(7):
        print(value)
        v = lista_datos[cont]
        if value == 6:
            cadena = cadena + "|{}".format(v)
        else:
            cadena = cadena + "{}".format(v) + ","
        cont = cont + 1

    lista_json.append(cadena)




lista_json = [23,23,23,2,3,3,3,4]

# Escribir 
file = open('lost_datos.txt', 'wb')
file.write()
file.close()

