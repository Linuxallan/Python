import imp
import json
import boto3

# 'paginar users' --> 'enumerar usuarios' (listar)

iam = boto3.client('iam')

try:
    # Crear usuario
    response = iam.create_user(
        UserName= 'user_sdk'
    )
    print(response)
except Exception as error:
    print(error)

# listar usuarios
paginator = iam.get_paginator('list_users')
for response in paginator.paginate():
    print(response)

    # ---- Actualizar usuario
try:
    iam = boto3.client('iam')
    iam.update_user(
        UserName = 'user_sdk',
        NewUserName = 'user_SDK_created'
    )
except Exception as error:
    print(error)

# Eliminar usuario
try:
    iam.delete_user(
        UserName = 'user_sdk'
    )
except Exception as error:
    print(error)

try:
    iam.delete_user(
        UserName = 'user_SDK_created'
    )
except Exception as error:
    print(error)


# =============================================================
# Politicas

import boto3
import json

iam = boto3.client('iam')

# Crear politica
my_managed_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:DeleteItem",
                "dynamodb:GetItem",
                "dynamodb:PutItem",
                "dynamodb:Scan",
                "dynamodb:UpdateItem"
            ],
            "Resource": "*"
        }
    ]
}

try:
    response = iam.create_policy(
        PolicyName = 'JJJmyDynamoDBPolicy',
        PolicyDocument = json.dumps(my_managed_policy)
    )
except Exception as error:
    print(error)

print(response)

# obtener politica especifica por su ARN
response = iam.get_policy(
    PolicyArn = 'arn:aws:iam::503208849944:policy/JJJmyDynamoDBPolicy'
)
print('Politica:',response['Policy'])

# ------------
# Trust policy Lambda
my_trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],
            "Principal": {
                "Service": [
                    "lambda.amazonaws.com"
                ]
            }
        }
    ]
}
# Asociar politica a rol y crear rol
# 'PermissionsBoundary' : son los permisos maximos que la entidad podra asumir.
# --> ver como no asignar ninguna 'PermissionsBoundary'.
try:
    response = iam.create_role(
        Path='/',
        RoleName='JJJ-Role_SDK',
        AssumeRolePolicyDocument=json.dumps(my_trust_policy),
        Description='Role de prueba SDK python',
        MaxSessionDuration=3600,
        PermissionsBoundary='arn:aws:iam::503208849944:policy/lambda-reed-ec2-and-ebs',
        Tags=[
            {
                'Key': 'Envaironment',
                'Value': 'Dev'
            },
        ]
    )
except Exception as error:
    print(error)

# Atar politica a rol
# 'PolicyArn' : arn de la politica a atar.
# 'RoleName' : nombre del ro, que asumira la politica.
iam.attach_role_policy(
    PolicyArn = 'arn:aws:iam::503208849944:policy/service-role/AWSLambdaBasicExecutionRole-0f6f80be-8e0b-4f7f-bbd8-f2d61281853a',
    RoleName = 'JJJ-Role_SDK'
)

# Quitar politica a role
iam.detach_role_policy(
    PolicyArn = 'arn:aws:iam::503208849944:policy/service-role/AWSLambdaBasicExecutionRole-0f6f80be-8e0b-4f7f-bbd8-f2d61281853a',
    RoleName = 'JJJ-Role_SDK'
)
