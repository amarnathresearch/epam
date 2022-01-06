# import boto3


# response = s3.list_objects(Bucket='amarnathsample')

# s3.upload_file(Filename='/home/amarnath/Downloads/X.pdf', Bucket='amarnathsample', Key='sample/sample.pdf')
# print(response)

import boto3
import os


s3 = boto3.client("s3", 
                  region_name='us-east-1', 
                  aws_access_key_id='', 
                  aws_secret_access_key='')

path = '/home/amarnath/Documents/Epam/exercises/screenshots/'
for f in os.listdir(path):
    s3.upload_file(Filename=path+f, Bucket='amarnathsample', Key='sample/'+f)
