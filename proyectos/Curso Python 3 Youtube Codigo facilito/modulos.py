# Al importar se usa la funcion por medio del archivo importado
import calculadora
print(calculadora.suma(23, 55))
""" El archivo '__pycache__' contiene un archivo de compilacion 
que vuelve mas rapida la ejecucion del 'import' importanto datos
de otro archivo
"""

# usar from se usa la funcion importada directamente, NO POR MEDIO DEL ARCHIVO
from calculadora import rest 
print(rest(35, 77))

# redefinir nombre de funcion importada
# from calculadora import * (queda No claro lo que se importa)
from calculadora import suma as sumemos
print(sumemos(45, 80))

## __name__ devuelve el script principal
print(__name__) # esto devuelve '__main__'
if __name__ == "__main__": # Lo que pregunta es si este script es el principal: el que ejecuta a todos.
    pass