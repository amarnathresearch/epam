import boto3

ec2 = boto3.client('ec2', region_name = 'ap-south-1', aws_access_key_id='', 
                  aws_secret_access_key='')
response = ec2.describe_instances()
print(response)


# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html

try:
    ec2.stop_instances(InstanceIds=['',''], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        raise

try:
    ec2.start_instances(InstanceIds=['',''], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        raise