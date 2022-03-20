# Este archivo hace que el compilador reconosca la carpeta 'paquete_animals' como
# un paquete.

# Aqui se importan todo lo que se necesite exportar.
# '.gato'  : buscar 'gato' en el mismo nivel.
from .gato import Gato

# se pueden crear funciones y lo que sea en este archivo y usarse importandolas
# desde el otro archivo
def generar_gato(nombre):
    return Gato(nombre)