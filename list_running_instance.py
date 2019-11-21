#!/usr/bin/env python
import boto3

detail = []
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances :
    print(instance)
    print (instance.id, instance.state)
    detail.append = instance.Name
    print(detail)
    







