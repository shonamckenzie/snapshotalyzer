import boto3
import click

s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2')

@click.command()
def list_instances():
  "List EC2 instances"
  for i in ec2.instances.all():
    print(', '.join((
      i.id,
      i.instance_type,
      i.placement['AvailabilityZone'],
      i.state['Name'],
      i.public_dns_name)))
  return

def list_buckets():
  "List S3 buckets"
  for bucket in s3.buckets.all():
    print(bucket.name)

if __name__ == '__main__':
  list_instances()