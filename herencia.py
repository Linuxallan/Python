"""
Herencia de clases a varios niveles.
Herencia multiple.
"""
class Animal:
    @property
    def terrestre(self):
        return True

class Felino(Animal):

    def cazar(self):
        return "El felino esta cazando"
    
    """
    # Este Method es privado solo para la clase Felino
    # por lo que las clases hijas no pueden heredarla.
    def __cazar(self): # Private Method.
        return "El felino esta cazando"
    """
    
    @property # Transforma metodo de abajo en propiedad
    def tiene_garras(self):
        return True

class Mascota:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
    @property
    def get_nombre(self):
        return self.nombre

# Herencia Multiple
class Gato(Felino, Mascota):

    def __init__(self, nombre):
        # LLamar method __init__ de Mascota antes del propio de este method.
        Mascota.__init__(self, nombre) 
        self.nombre = nombre

class Jaguar(Felino):
    pass

# Gato pide atributo de Herencia 2
gato = Gato("Chester")
jaguar = Jaguar()
# Gato accede a herencia 1
print(gato.cazar())
# Gato accede a herencia 2
print(gato.nombre)
print(jaguar.tiene_garras)
# acceder a method de clase nivel 3 hacia arriba.
print(jaguar.terrestre)