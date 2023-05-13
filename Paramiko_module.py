#Paramiko_module.py

import paramiko
#used to work with remote severs
#we need ssh protocal on the local machine
print("working with the paramiko module")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect(hostname='43.205.135.52',username='paramiko',password='paramiko123',port=22)
# ssh.connect(hostname='15.207.108.204',username='Administrator',password='AbJ1A.Hxa.L3;XI%agOU-az38wEnxj)4',port=3389,banner_timeout=200)
stdin, stdout, stderr = ssh.exec_command('ls')
print("The output of the command: ")
# sftp_client=ssh.open_sftp()
# sftp_client.get('/home/paramiko/paramiko_download.txt','paramiko_downloaded.txt' )
print(stdout.read())

print(stderr.read())
# sftp_client.close()
ssh.close()
