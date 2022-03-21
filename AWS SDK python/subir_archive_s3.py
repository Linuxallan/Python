import boto3
from botocore.client import Config

BUCKET_NAME = 'qse503208849944'

img = "./img_video/catalina.png"

s3 = boto3.resource('s3')
data = open(img, 'rb')

s3.Bucket(BUCKET_NAME).put_object(key='catalina.png', body=data)

print("Done")