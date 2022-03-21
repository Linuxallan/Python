"""
Descargar archivos pesados. Chunks: descarga por porciones manteniendo la
conexion abierta y cerrandola manualmente.

En este ejemplo se descarga un video con extencion 'mp4' de los servidores de 'imgur'.
Es interesante por que la descarga dura algunos segundo en lo que laconexion 
se mantiene abierta, luego al finalizar se cierra automaticamente.
El argumento : 'stream':True --> es muy importante.
La funcion: iter_content() es como un yield --> que descarga porciones y las 
almacena temporalmente y al final entrega todo los datos junto como uno.
"""
import requests
import json

if __name__ == '__main__':

    url = 'https://i.imgur.com/JdDvJXi.mp4'
    # El argumento 'stream':True --> lo que hace es dejar la conexion
    # abierta para poder descargar archivos grandes.
    # Esto requiere que uno sea el responsable de cerrar la conexion.
    args = {'stream':True}

    response = requests.get(url, params=args)
    with open('videoimgur.mp4', 'wb') as file:
        # iter_content toma el video de internet y lo descarga poco a poco.
        for chunk in response.iter_content(): # Descarga por porciones.
            file.write(chunk)

    # Cerrar la conexion
    response.close()