"""
En esta request 'POST' los datos de la request de respuesta son diferentes
a la de la request 'GET'
"""
import json
import requests

if __name__ == '__main__':

    url = 'http://httpbin.org/post'
    args = {'nombre':'Alan', 'curso':'Python APIs'}
    payload = {'dato1':'brazil', 'dato2': 34, 'dato3':'rusia'}
    # El Token de Autenticacion se debe mandar en el Encabezado: headers
    # No en la URL ni en los Argumentos.
    headers = {'Content-Type': 'application/json', 'Access-Token':'E1234E'}

    # Serializar los datos: 'json.dumps()' --> si no se hace esto los datos
    # se mandaran de vuelta en un modulo 'form' y no queremos eso.
    #response = requests.post(url, params=args, data=json.dumps(payload))
    response = requests.post(url, params=args, json=payload, headers=headers)

    if response.status_code == 200:

        # Asignacion de la 'request' a un archivo json para poder leerlo bien.
        content = response.content
        file = open('request_json.json', 'wb')
        file.write(content)
        file.close()
        #print(response.content)

        # Manera 1 de obtener los datos de un modulo de la request
        response_json = response.json()
        headers_json = response_json['headers']
        print("Headers: ", headers_json)
        # Manera 2 de obtener los datos de un modulo de la request
        # Este me da Encabezados diferentes al anterior
        headers_json = response.headers
        print("Headers 2: ", headers_json)
        # Acceder a SubEncabezados
        server = headers_json['server']
        print("Server: ", server)

