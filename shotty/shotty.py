import boto3

if __name__ == '__main__':
  s3 = boto3.resource('s3')
  for bucket in s3.buckets.all():
      print(bucket.name)
  ec2 = boto3.resource('ec2')
  for i in ec2.instances.all():
      print(i)