# Subir un nivel atras se hace con dos puntos mas el nombre del archivo o carpeta: 
# '..bla...' 
from ..terrestres import CelulasTerrestres

class CelulaInorganica(CelulasTerrestres):

    def __init__(self, nombre):
        self.nombre = nombre