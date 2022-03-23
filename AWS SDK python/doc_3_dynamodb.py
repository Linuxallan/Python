import boto3

dynamodb = boto3.resource('dynamodb')

try:
    # Crear tabla
    table = dynamodb.create_table(
        TableName = 'users',
        KeySchema = [
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'last_name',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions = [
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'last_name',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    table.wait_until_exists()

    print(table.item_count) 
except Exception as error:
    print(error)


# Obtener una tabla especifica
table = dynamodb.Table('users')
print('Tiempo: ',table.creation_date_time)

# Agregar Item a la tabla
table.put_item(
    Item={
        'username': 'pyAlan',
        'first_name': 'Alan',
        'last_name': 'python',
        'age': 25,
        'account_type': 'standard_user',
    }
)
print(table.item_count) 

# Obtener un item
response = table.get_item(
    Key = {
        'username': 'pyAlan',
        'last_name': 'python',
    }
)
item = response['Item']
print(item)

# Update item especifico
table.update_item(
    Key = {
        'username': 'pyAlan',
        'last_name': 'python',
    },
    UpdateExpression = 'SET age = :vall',
    ExpressionAttributeValues = {
        ':vall': 29
    }
)

# Obtener un item
response = table.get_item(
    Key = {
        'username': 'pyAlan',
        'last_name': 'python',
    }
)
item = response['Item']
print(item)

# Eliminar item
table.delete_item(
    Key = {
        'username': 'pyAlan',
        'last_name': 'python',
    }
)

# insertar items por lotes
with table.batch_writer() as batch:
    for i in range(50):
        batch.put_item(
            Item={
                'account_type': 'anonymous',
                'username': 'user' + str(i),
                'first_name': 'unknown',
                'last_name': 'unknown'
            }
        )

### ===================== Queryes ====================
from boto3.dynamodb.conditions import Key, Attr

response = table.query(
    KeyConditionExpression = Key('username').eq('user12')
)
items = response['Items']
print(items)


"""
Este 'SCAN' busca a todos los usuario cuyo 'first_name' comience con 'J'
y cuyo 'account_type' sea 'super_user'.
Aqui hay una condicion 'IF'.
"""
response = table.scan(
    FilterExpression=Attr('first_name').begins_with('J') & Attr('account_type').eq('super_user')
)
items = response['Items']
print(items)


# Eliminar items por lotes
with table.batch_writer() as batch:
    for i in range(50):
        batch.delete_item(
            Key={
                'username': 'user' + str(i),
                'last_name': 'unknown'
            }
        )

table.delete()