import boto3
# =====================================
# Crear alarma si no existe
# Actualiza la alarma si ya existe la alarma con el nombre:
# 'Web_Server_CPU_Utilization'

cw = boto3.client('cloudwatch')

cw.put_metric_alarm(
    AlarmName='Web_Server_CPU_Utilization',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=60,
    Statistic='Average',
    Threshold=70.0,
    ActionsEnabled=False,
    AlarmActions=[
      'arn:aws:swf:us-west-2:503208849944:action/actions/AWS_EC2.InstanceId.Reboot/1.0'
    ],
    AlarmDescription='Alarm when server CPU exceeds 70%',
    Dimensions=[
        {
          'Name': 'InstanceId',
          'Value': 'INSTANCE_ID'
        },
    ],
    Unit='Seconds'
)
# deshabilitar action de la alarma: 'Web_Server_CPU_Utilization'
cw.disable_alarm_actions(
  AlarmNames=['Web_Server_CPU_Utilization'],
)

#-----------------
# Mostrar lista de alarmas
cw = boto3.client('cloudwatch')

# Traer una lista de todas las alarmas
paginator = cw.get_paginator('describe_alarms')

for response in paginator.paginate(StateValue='INSUFFICIENT_DATA'):
    res = response['MetricAlarms']
    print("Metrica: {} \n".format(res))


# Eliminar especifica alarma
cw.delete_alarms(
    AlarmNames = ['Web_Server_CPU_Utilizationn'],
)

# Listar metricas de la alarma
paginator = cw.get_paginator('list_metrics')
for response in paginator.paginate(Dimensions=[{'Name':'LogGroupName'}],
                                    MetricName='IncomingLogEvents',
                                    Namespace='AWS/Logs'):
    print(response['Metrics'])


# Poner metricas, se ve en 'Metrics' en la consola grafica de AWS
# con el nombre del 'Namespace' : SITE/TRAFFIC.
cw = boto3.client('cloudwatch')

cw.put_metric_data(
    MetricData=[
        {
            'MetricName': 'PAGES_VISITED',
            'Dimensions': [
                {
                    'Name': 'UNIQUE_PAGES',
                    'Value': 'URLS'
                },
            ],
            'Unit': 'None',
            'Value': 1.0
        },
    ],
    Namespace = 'SITE/TRAFFIC'
)

cw.delete_alarms(
    AlarmNames = ['Web_Server_CPU_Utilization'],
)