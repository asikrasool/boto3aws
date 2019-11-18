import boto3

ecs = boto3.client("ecs")

response = ecs.list_clusters()
print(response)
