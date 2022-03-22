from urllib import response
import boto3

# Instanciar objeto tipo recurso 's3'
s3 = boto3.resource('s3')

# Recorrer lista de todos los buckets y por cada uno imprimir su nombre.
for bucket in s3.buckets.all():
    print(bucket.name)

# =======================================================
# SQS tutorial

sqs = boto3.resource('sqs')

# Crear SQS
queue = sqs.create_queue(QueueName='test_1', Attributes={'DelaySeconds' : '5'})

print(queue.url)
print(queue.attributes.get('DelaySeconds'))

# Ver Queue por su nombre
try:
    queue = sqs.get_queue_by_name(QueueName='test_1')
    print(queue.url)
except Exception as error:
    print("Error:", error)

# Listar todos lo Queue
try:
    for queue in sqs.queues.all():
        name = queue.attributes['arn:aws:sqs:us-west-2:503208849944:test_1'].split(':')[-1]
        print(name)
except Exception as error:
    print(error)

#------------------
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='test_1')

# mandar mensaje
response = queue.send_message(MessageBody='Helloworld')
print("Message ID:",response.get('MessageId'))
print(response.get('MD5OfMessageBody'))

# mandar message con datos personalozados
response = queue.send_message(MessageBody="What's up", MessageAttributes={
    'Author': {
        'StringValue': 'Alan',
        'DataType': 'String'
    }
})
print("Message ID:",response.get('MessageId'))
print(response.get('MD5OfMessageBody'))

# Enviar listas de datos personalozados
try:
    response = queue.send_messages(Entries=[
        {
            'Id': '1',
            'MessageBody': 'Man'
        },
        {
            'Id': '2',
            'MessageBody': 'boto3 eee',
            'MessageAttributes': {
                'Author': {
                    'StringValue': 'Alan',
                    'DataType': 'String'
                }
            }
        }
    ])
except Exception as error:
    print('Error:', error)
print('Failed:',response.get('Failed'))
print('Seccess:',response.get('Successful'))

# ==================================
# Procesar message Queue
try:
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='test_1')

    for message in queue.receive_messages(MessageAttributeNames=['Author']):

        author_test = ''
        if message.message_attributes is not None:

            author_name = message.message_attributes.get('Author').get('StringValue')

            if author_name:
                author_test = ' ({0})'.format(author_name)
        
        print("Hello {0} ,{1}".format(message.body, author_test))

        message.delete()
except Exception as error:
    print('Error: ', error)

# Eliminar queue creado
queue.delete()