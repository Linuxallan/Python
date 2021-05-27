men = "Def"

def mensaje(men):
    print("Hao")
    print(men)

# Si la funcion tiene parametros, al llamarse debe escribirse tambien el nombre
# de los parametros.
mensaje(men)

def suma():
    varr = 3++4
    print(varr)

suma()

# num1 y num2 no estan definidos como variables, sino que solo o estan
# como parametros a los que se les puede asignar valor.
def sinDef(num1, num2):
    if num1 > num2:
        print("num 1 is the best by: ", num1-num2)
    else:
        print("2 es mayor por: ", num2-num1)

    return print("total: ", num1+num2)

sinDef(11, 7)
sinDef(7, 13)

# ----------------------- De una segunda manera escribir el 'return'--------
def sinDef(num1, num2):
    if num1 > num2:
        print("num 1 is the best by: ", num1-num2)
    else:
        print("2 es mayor por: ", num2-num1)

    return "total: ", num1+num2

sinDef(7, 13)

# Se puede imprimir el 'return' de una funcion 'def'
print(sinDef(7, 13))

# Se puede guardar todo el valor que devuelve el 'return' de una funcion 'def'
varGuardar = sinDef(4,99)
print(varGuardar)