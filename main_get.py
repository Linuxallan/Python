"""
En esta request 'GEt' los datos de la request de respuesta son diferentes
a la de la request 'POST'
"""
import requests

"""
Primera esctructura basica de solicitud GET usando una URL y la libreria REQUEST.
"""
if __name__ == '__main__':

    # Los argumentos pueden agregarse direcyamente en la URL despues de un '?'
    #url = 'https://www.google.com.mx?param1=soy+un+parametro'
    url = 'https://www.google.com.mx'
    response = requests.get(url)
    
    # 'status_code' : valida el estatus de la respuesta obtenida de la peticion.
    if response.status_code == 200:
        # 'content' retorna todo el contenido HTML de la peticion, osea la pagina
        # HTML a la cual accedio con la peticion
        ### print(response.content)

        # Almacenar todo el contenido HTML en un archivo propio
        content = response.content
        # primer parametro es nombre del archivo a crear, el segundo parametro 
        # significa write binary: escritura binaria.
        file = open('google.html', 'wb')
        file.write(content)
        file.close()


"""
Second ejemplo a una web que returna un JSON con varios datos y parametros
"""
import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    args = {'nombre':'Alan', 'curso':'Python APIs'}

    response = requests.get(url, params=args)

    if response.status_code == 200:

        # Escribir el json obtenido en un archivo json : 'request_json.json'
        content = response.content
        file = open('request_json.json', 'wb')
        file.write(content)
        file.close()

        # Leer la URL final de la 'request'
        print("URL : ", response.url)

        # Leer la 'request' y convertirla a diccionario
        response_json = response.json() # Diccionario
        # Ahora puedo acceder a cualquier modulo de la peticion
        headers = response_json['headers']
        print("Headers : ", headers)
        # Accedo al modulo de la peticion 'origin'
        origin = response_json['origin']
        print("Origins : ", origin)

        ### ---- Acceder a los moulos de la request usando la libreria 'json'
        response_json = json.loads(response.text)
        args_json = response_json['args']
        print("ARGS desde JSON : ", args_json)
        
        