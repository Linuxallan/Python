"""
Esta funcion crea una instancia de cliente para el servicio's3'
y hace una peticion para obtener los nombres de todos lo buckets
de una region.
Usa un Rol de : 'awss3fullaccess' para funcionar el cual se agrega 
a los permisos ya existentes de la funcion lambda.
"""
import json
import boto3

def lambda_handler(event, context):
    
    s3 = boto3.client('s3')
    list_obj_summary = s3.list_buckets()
    
    lista = []
    
    for obj_sum in list_obj_summary["Buckets"]:
        lista.append(obj_sum["Name"])
        print(obj_sum)
        
    return {
        'statusCode': 200,
        'body': json.dumps(lista)
    }
