import boto3
import json

sts_client = boto3.client('sts')
AWS_ACCOUNT_ID = '160580700920'
ROLE_NAME = 'ec2-demo-role'

assumed_role_object=sts_client.assume_role(
    RoleArn = f'arn:aws:iam::{AWS_ACCOUNT_ID}:role/{ROLE_NAME}',
    RoleSessionName = "AssumeRoleSession1"
)
credentials = assumed_role_object['Credentials']

client = boto3.client(
    'ec2',
    region_name = "us-east-1",
    aws_access_key_id = credentials['AccessKeyId'],
    aws_secret_access_key = credentials['SecretAccessKey'],
    aws_session_token = credentials['SessionToken']
)


response = client.describe_instances()

for dic in response['Reservations']:
    num = 0
    my_desc = dic['Instances'][num]['State']
    if 'stopped' in my_desc.values():
        print ("Stopped")
        print (dic['Instances'][num]['InstanceId'])
    else:
        print ("Running")
        print (dic['Instances'][num]['InstanceId'])
    num +=1