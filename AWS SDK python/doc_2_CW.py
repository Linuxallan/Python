import boto3
# =====================================
# Crear alarma si no existe
# Actualiza la alarma si ya existe la alarma con el nombre:
# 'Web_Server_CPU_Utilization'

cw = boto3.client('cloudwatch')

cw.put_metric_alarm(
    AlarmName='Web_Server_CPU_Utilizationn',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=60,
    Statistic='Average',
    Threshold=70.0,
    ActionsEnabled=False,
    AlarmDescription='Alarm when server CPU exceeds 70%',
    Dimensions=[
        {
          'Name': 'InstanceId',
          'Value': 'INSTANCE_ID'
        },
    ],
    Unit='Seconds'
)

#-----------------
# Mostrar lista de alarmas
cw = boto3.client('cloudwatch')

# Traer una lista de todas las alarmas
paginator = cw.get_paginator('describe_alarms')

for response in paginator.paginate(StateValue='INSUFFICIENT_DATA'):
    res = response['MetricAlarms']
    print("Metrica: {} \n".format(res))
