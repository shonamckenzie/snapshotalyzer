from setuptools import setup

setup(
  name='snapshotalyzer',
  version='0.1',
  description='Snapshotalyzer is a tool to manage creation of EC2 snapshots',
  license='GPLv3+',
  packages=['shotty'],
  url='https://github.com/shonamckenzie/snapshotalyzer',
  install_requires=[
    'click',
    'boto3'
  ],
  entry_points='''
  [console_scripts]
  shotty=shotty.shotty:cli
  ''',
)