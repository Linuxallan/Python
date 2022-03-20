"""
Methodos Magicos que estan disponibles para cualquier instancia de
cualquier clase creada.
Estos Mthods se ejecutan automaticamente al instanciar y al llamar 
al objeto.
"""

class Usuario:

    # Este metodo '__new__' es el constructor de la clase
    # y el primero en ejecutarse.
    # OJO : No usa 'self', sino: 'cls'.
    def __new__(cls):
        print("Method __new__ es el constructor de la clase")
        return super().__new__(cls)

    def __init__(self):
        print("Method __init__ es el segundo en ejecutarse al instanciar la clase")

    # Este Method Magico 
    def __str__(self):
        return "Este Method Magico se muestra al mostrar el objeto completo de la instancia"
    
    # Este method modifica comportamiento.
    def __getattribute__(self, nombre):
        print("no se encontro el atributo nombre")

user = Usuario()
print(user)