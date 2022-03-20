# Subir dos niveles atras para ir a buscar una clase.
# se usa : dos puntos '..bla...' antes del nombre del alrchivo o carpeta.
from ..terrestres import CelulasTerrestres

class CelulaOrganica(CelulasTerrestres):

    def __init__(self, nombre):
        self.nombre = nombre