import json
import boto3

region = 'us-east-1'
instances = ['']

ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print(f"Starting instances: {str(instances)}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }