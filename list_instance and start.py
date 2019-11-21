import boto3
ec2 = boto3.resource('ec2')
detail = []
for instance in ec2.instances.all():
    print(instance.id, instance.instance_type,instance.state)
    detail.append(instance.id)
    print(detail)


ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds = detail).start() #for starting an ec2 instance
print(instance.id, instance.instance_type,instance.state)






