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

    try:
        f = open('lost_datos.json')
        data = json.load(f)
        f.close()

        return data
    except Exception as error:
        print("Error: No datos en el json: (exception) ", error)
        vasio = []
        return vasio

def jsonFormat(data, lista):  

    try:
        indice = len(data.items()) +1
        
    except Exception as error:
        indice = 1

    json_temp = json.dumps(lista)
    json_listo = '"'+str(indice)+'"' + ':' + json_temp

    return json_listo
    

def imprimir_json(data, jjson):

    f = ""
    if(len(data)== 0):
        f = '{' + jjson + '}'
    else:
        ddata = json.dumps(data)

        dddata = ddata.replace('}', '')
        
        f = dddata + ',' + jjson + '}'

    file = open('lost_datos.json', 'wb')
    file.write(f.encode())
    file.close()    

while (True):

    data = leerjson()        

    count = 1
    tempo_datos = []
    print("-----------------------------------------------------")
    print("-----------------------CHEKED------------------------")
    print("-----------------------------------------------------")

    while count <= 6:
        
        print("Ingrese Numero")
        print(".....................")
        num = input()
        tempo_datos.append(num)
        count = count + 1
    
    json_listo = jsonFormat(data, tempo_datos)

    imprimir_json(data, json_listo)



"""
    #for key in data.values():  IMPRIMIR CADENA DE NUMEROS
    #for key in data.keys():    IMPRIMIR INDICE
    for key in data.items():
        
        #val = data[key]
        #print(val)
        print(key)
    """


"""
{
    "1": [
        12,
        34,
        21,
        1,
        5,
        33
    ],
    "2": [
        ...
        ...
        ...
    ]
}
"""
"""
{
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
}
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