import paramiko

host = "my.host.com.br"
transport = paramiko.Transport((host))
username = "username"
mykey = paramiko.RSAKey.from_private_key_file("key.pem")

print ("Connecting...")
transport.connect(username = username, pkey = mykey)
sftp = paramiko.SFTPClient.from_transport(transport)
print ("Connected.")
print (sftp.listdir())
files = sftp.listdir('/processed')
for i, file in enumerate(files):
    if file and file.startswith('20230124'):
        sftp.get(f'/processed/{file}', f'{file}')
sftp.close()
transport.close()
print ("Closed connection.")


