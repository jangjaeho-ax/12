import sys
import boto3
from botocore.exceptions import ClientError
import paramiko
import os
HOST= '13.124.192.64'
ID ='ec2-user'
PASSWD =''
key = paramiko.RSAKey.from_private_key_file(".\\TEST.pem")
ssh= paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname= HOST, username= ID, pkey=key)

stdin, stdout, stderr = ssh.exec_command('echo "hello"')
stdin.close()

for line in stdout.read().splitlines():
    print(line.decode())

ssh.close()