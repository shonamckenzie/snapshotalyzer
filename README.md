# snapshotalyzer

Demo project to manage AWS EC2 instance snapshots

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

shotty uses the configuration file created by the AWS cli. 

## Running

`pipenv run "python shotty/shotty.py <command> <subcommand> <--project=PROJECT>"`

*command* is instances, volumes, or snapshots
*subcommand* - depends on command
*project* is optional

## Distribution package

Rather than clone the repo, distribution package has been created and is available to install via pip: 

`pip3 install https://snapshotalyser-dist.s3.eu-west-2.amazonaws.com/snapshotalyzer-0.1-py3-none-any.whl`

`shotty --help` gives you the list of commands available

