import boto3

session = boto3.Session(aws_access_key_id='', aws_secret_access_key='')

resource = session.resource('s3')

client = session.client('s3')

print(resource)
print(client)





