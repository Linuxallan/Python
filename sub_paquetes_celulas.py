# Aqui no se usa punto '.' al hacer referencia al nombre
# de una carpeta del mismo nivel.
# A diferencia del segundo nivel que la referencia a la carpeta 
# se hace desde un archivo '__init__.py'.
from sub_paquetes_celulas import CelulaOrganica
from sub_paquetes_celulas import CelulaInorganica

celula_organica = CelulaOrganica("OrganicCel")
celula_inorganica = CelulaInorganica("InorCel")

print(celula_organica.nombre)
print(celula_inorganica.nombre)