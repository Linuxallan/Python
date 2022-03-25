import json
from urllib import response
import boto3
from grpc import Status
from sympy import re

# crear usuario
iam = boto3.client('iam')

try:
    response = iam.create_user(
        UserName='user-SDK'
    )
    print("User created")
except Exception as error:
    print(error)

# Listar claves de acceso
"""
Este for  lista las claves de acceso de usuario y yo valido cuantas
tiene para solo permitir que se creen claves de acceso solo si previamente
no tiene ninguna.
Solo permito crear una Claves de acceso por usuario.
PD : IAM permite un maximo de 2 Access Keys por usuario por defecto.
"""
paginator = iam.get_paginator('list_access_keys')
for paginator in paginator.paginate(UserName='user-SDK'):
    if len(paginator) > 1:
        print("Ya tiene una Acces Key")
        print(len(paginator))
    else:
        # asignar claves de acceso a usuario
        try:
            response = iam.create_access_key(
                UserName='user-SDK'
            )
            print("Access Keys creadas y asignadas al usuario")
        except Exception as error:
            print(error)


# Obtener ultima ves del acces key usada por el usuario
try:
    response = iam.get_access_key_last_used(
        AccessKeyId='AKIAXKKMVWIMCMX7PYKZ'
    )
    print("Ultimo uso: ", response)
except Exception as error:
    print(error)

# Actualizar el estado 'status' de una access key
try:
    response = iam.update_access_key(
        AccessKeyId='AKIAXKKMVWIMD5SBBNI7',
        Status='Inactive',
        UserName='user-SDK'
    )
    print("Access Keys Actualizada")
except Exception as error:
    print(error)

# Eliminar access keys
try:
    response = iam.delete_access_key(
        AccessKeyId='AKIAXKKMVWIMD5SBBNI7',
        UserName='user-SDK'
    )
    print("Access Keys Eliminada")
except Exception as error:
    print(error)
