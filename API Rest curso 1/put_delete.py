import requests
import json

# Method PUT : Actualizar
if __name__ == '__main__':

    url = 'http://httpbin.org/put'
    args = {'nombre':'Alan', 'curso':'Python APIs'}
    payload = {'dato1':'brazil', 'dato2': 34, 'dato3':'rusia'}
    headers = {'Content-Type': 'application/json', 'Access-Token':'E1234E'}

    response = requests.put(url, params=args, json=payload, headers=headers)

    if response.status_code == 200:

        content = response.content
        file = open('request_json.json', 'wb')
        file.write(content)
        file.close()

if __name__ == '__main__':

    url = 'http://httpbin.org/delete'
    args = {'nombre':'Alan', 'curso':'Python APIs'}
    payload = {'dato1':'brazil', 'dato2': 34, 'dato3':'rusia'}
    headers = {'Content-Type': 'application/json', 'Access-Token':'E1234E'}

    response = requests.delete(url, params=args, headers=headers, json=payload)

    if response.status_code == 200:
        content = response.content
        file = open('request_json.json', 'wb')
        file.write(content)
        file.close()