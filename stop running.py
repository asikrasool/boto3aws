import boto3

ec2 = boto3.resource('ec2')
instance = ec2.instances.filter(InstanceIds = ['INSTANCE_ID']) #for stoping an ec2 instance
print(instance)




ec2.instances.filter(Filters= [
    {'Name' : 'instance-state-name',
     'Values' : 'running'
     }
    ]).stop   #for stoping an ec2 instance



ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)
