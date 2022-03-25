from pydoc import cli
import boto3
import json

cliente = boto3.client('billingconductor')

#print(cliente.get_paginator('get_paginator'))