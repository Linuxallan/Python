"""
Me surge un error por que al re leer el archivo json que queda mal escrito
despues de registrar datos, este arroja una error, solo eso.

1. Subir una capa de desarrollo: hacer la capa contenedora de la cadena json
que se va agregando en cada registro.
--> hacer: "[ "1": { ... }, "2": { ...}]"
--> probar en una grafico en web que funcione el json total de los datos
"""
import json

lista_datos = []

def leerjson():

    f = open('lost_datos.json')
    data = json.load(f)
    f.close()

    return data

def jsonFormat(lista):  

    dicc = {'a': lista[0], 'b': lista[1], "c": lista[2], 'd': lista[3], 'e': lista[4], 'f': lista[5]}
    json_listo = json.dumps(dicc)

    return json_listo

def imprimir_json(data, jjson):

    ddata = json.dumps(data)
    f = ddata + ',' + jjson
    file = open('lost_datos.json', 'wb')
    file.write(f.encode())
    file.close()    

while (True):

    data = leerjson()

    count = 1
    tempo_datos = []
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")

    while count <= 6:
        
        print("Ingrese Numero")
        print(".....................")
        num = input()
        tempo_datos.append(num)
        count = count + 1
    
    json_listo = jsonFormat(tempo_datos)

    imprimir_json(data, json_listo)



"""
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
"""


"""
"numbers": [
    "1": {
        "a": 12,
        "b": 34,
        "c": 21,
        "d": 1,
        "e": 5,
        "f": 33
    },
    "2": {
        ...
        ...
        ...
    }
]
"""

"""
def jsonFormat(lista):  

    _json = ""

    for value in range(1,6):

        letra = ""
        if (value == 1):
            fila = '{ "{}": {},'.format(letra, value)
            letra = "a"
        elif (value == 2):
            letra == "b"
        elif (value == 3):
            letra = "c"
        elif (value == 4):
            letra = "d"
        elif (value == 5):
            letra = "e"
        else:
            letra = "f"
            fila = '{ "{}": {} },'.format(letra, value)
            _json = _json + '{ "' + letra + '": ' + value + ' },'

        if (value != 1 || value != 6):

            fila = '{ "{}": {},'.format(letra, value)
            _json = _json + fila
    
    return _json
"""