import boto3

# lambda --> palabra reservada
lambda_client = boto3.client('lambda')

response = lambda_client.create_function(

    FunctionName = 'lambda-created-from-studiocode-with-sdk-python',
    Runtime = 'python 3.9',
    Role = 'string',
    Handler = '',
    Code = {

    },
    Description = '',
    Timeout = 60,
    MemorySize = '',
    Publish = 'False',
    VpcConfig = {
        
    }
    
)









"""
# Agregar Politica basada en recurso.
response = lambda_client.add_permission(
    FunctionName='arn:aws:lambda:us-west-2:503208849944:function:SDKs-test-one',
    StatementId = 'state_two',
    Action = 'lambda:GetFunction',
    Principal = 'arn:aws:iam::503208849944:user/acortes',
    SourceArn = 'arn:aws:lambda:::*',
    SourceAccount = '503208849944',
    # Token para las funciones de Alexa
    #EventSourceToken = '',
    # Especificar version de la funcion para solo agregar persmisos a esa version
    #Qualifier = '',
    #
    #RevisionId ='',
    # torgar persmiso a todas las cuentas bajo esa esta organizacion
    #PrincipalOrgID = ''
)

print(response)
"""

## Agregar paermiso para que la cuenta '503208849944' invoque una funcion
## lambda llamada 'SDKs-test-one'
response = lambda_client.add_permission(
    Action= 'lambda:InvokeFunction',
    FunctionName = 'arn:aws:lambda:us-west-2:503208849944:function:SDKs-test-one',
    Principal = '503208849944',
    StatementId = 'xaccount'
)
print(response)
# Queda pendiente invocar function.


