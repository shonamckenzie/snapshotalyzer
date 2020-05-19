import boto3
import click

s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2')

def filter_instances(project):
  instances = []

  if project:
    filters = [{'Name': 'tag:Project', 'Values':[project]}]
    instances = ec2.instances.filter(Filters=filters)
  else:
    instances = ec2.instances.all()
  return instances

@click.group()
def instances():
  """Commands for instances"""

@instances.command('list')
@click.option('--project', default=None, help="Only instances for project(tag Project:<name>)")
def list_instances(project):
  "List EC2 instances"
  instances = filter_instances(project)

  for i in instances:
    tags = { t['Key']: t['Value'] for t in i.tags or [] }
    print(', '.join((
      i.id,
      i.instance_type,
      i.placement['AvailabilityZone'],
      i.state['Name'],
      i.public_dns_name,
      tags.get('Project', '<no project>'))))
  return

@instances.command('stop')
@click.option('--project', default=None, help="Only instances for project(tag Project:<name>)")
def stop_instances(project):
  "Stop EC2 instances"
  instances = filter_instances(project)

  for i in instances:
    print("Stopping {0}...".format(i.id))
    i.stop()
  return

@instances.command('start')
@click.option('--project', default=None, help="Only instances for project(tag Project:<name>)")
def start_instances(project):
  "Start EC2 instances"
  instances = filter_instances(project)

  for i in instances:
    print("Starting {0}...".format(i.id))
    i.start()
  return

def list_buckets():
  "List S3 buckets"
  for bucket in s3.buckets.all():
    print(bucket.name)

if __name__ == '__main__':
  instances()