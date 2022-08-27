import boto3
import json

f = open('/etc/credential/credentials.json',)

# returns JSON object as
# a dictionary

data = json.load(f)
print("this is ston: ")
akey = data["access_key"]
sakey =  data["secret_access_key"]
region = data["region"]
print( akey, sakey, region)

#get to the account on aws:
session = boto3.session.Session(aws_access_key_id=akey,
                                aws_secret_access_key=sakey,
                                region_name=region)

ec2 = session.client('ec2')
region = 'us-east-2'
all_instances = ec2.describe_instances()

# print(json.dumps(all_instances['Reservations']))

print(all_instances['Reservations'][0]['Instances'][0]['InstanceId'])


instance_collector = []

for res in all_instances['Reservations']:
    for ins in res['Instances']:
        # print(ins['InstanceId'])
        instance_collector.append(ins['InstanceId'])
        # ec2_filter = [{'Name': 'instance-state-name', 'Values': ['terminated']}]
        # print(ec2_filter)
        # instance_collector.remove(ec2_filter)
print(instance_collector)

ec2.stop_instances(InstanceIds=instance_collector)
# To delete it, uncomment this.
# id_blat=['i-0792194a3a206bdfb']
# ec2.terminate_instances(InstanceIds=id_blat)


