from audioop import mul


def factorial_number(number_client):

    factorial = 1
    while number_client > 0:
        factorial = factorial * number_client
        number_client -= 1

    #print(factorial)
    return factorial

print(factorial_number(6))

# definir variables dentro siendo parametros
def sumar_numbers(valor_one = 12, valor_two = 34):
    return valor_one + valor_two

print(sumar_numbers())

# retorno de listas
def multiples_datos():
    return "string", 12, True, 2.4

print(multiples_datos())

# asignacion de listas a variables por funcion
string, number, bol, floa = multiples_datos()

## ----------------------------------
## Modificar valor localmente de una variable global
valor = "Soy Global de origen"
def modificar():

    global valor
    valor = "Modificada variable Global localmente desde funcion"

modificar()
print(valor)

## Crear variable global desde dentro funcion
def crear_var_global():
    global var_global
    var_global = 'Global desde function'

crear_var_global()
print(var_global)

## Argumentos : *args
# son para convertir en tupla todos los valores que entran de parametros
def convert_tupla_params(*args):
    return args

print(convert_tupla_params(1,45,'ertert',True,65,'fg4'))

# convertir a diccionario todos los parametros
def convert_diccionario_params(**kwargs):
    return kwargs
print(convert_diccionario_params(a=434, de='ef3', e33=False))
## * --> tuplas
## ** --> diccionarios


### ----------- LAMBDAS -------
funcion_lambda = lambda valor_one, valor_two: valor_one + valor_two
print(funcion_lambda(23, 6565))

lambda_two = lambda : 'solo retorna esto'
print(lambda_two())

## ------ closure
# funciones que crean funciones
def crear_funcion(num_one, num_two):

    def validar():
        return num_one > 0 and num_two > 0
    
    # NO : return validar()
    return validar

def ejecutar_otra_funcion(funcion):
    # NO : return funcion
    return funcion()
    
new_func = crear_funcion(3,65)
print(ejecutar_otra_funcion(new_func))

## ------------------------------
# ----- Decoradores
def decorador(funcion):
    funcion()

@decorador
def hola_mundo():
    print("Hola mundo decoradores")

#----
"""
# decorador pasando parametro y funcion
def decorer(value = False):
    def _decorer(funcion):
        funcion(value)
    _decorer

@decorer()
def saludo(value):
    if value:
        print("Hola s")
    else:
        print("ggg")
"""

## ------ Generadores
# alamcenar datos No en memoria (RAM)
def generador(*args):
    for valor in args:
        yield valor * 10
for dato in generador(2,45,65,77,8,9):
    print(dato)

"""
    La documentacion debe ir en la primera linea de la funcion
    para que sea reconocida por el interprete de python '__doc__
"""
def documentacion():
    """Esta es la documentacion de la funcion: documentacion
    """
    pass
doc = documentacion.__doc__
print(doc)
print(documentacion.__name__)