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


## Credit

This project was created using the [A Cloud Guru Python](https://acloud.guru/learn/python-for-beginners?_ga=2.238331974.758725971.1589876596-1463944726.1585083415&_gac=1.219418475.1589372453.CjwKCAjwte71BRBCEiwAU_V9h1rXUgFhbAvYDr1_zBU2abhWpgSNriH94J7kXTklHGxmDXFvLuuwUxoCkBQQAvD_BwE) course by Robin Norwood
