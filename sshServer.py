import paramiko
from io import BytesIO
from scp import SCPClient

class SHServer:
    def __init__(self, host, username, pswd):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.scp = SCPClient(self.ssh.get_transport())

        self.ssh.connect(host, 22, username, pswd)
        print("SSH соединение успешно установлено!")

        stdin, stdout, stderr = self.ssh.exec_command('ls -l')
        for line in stdout:
            print(line.strip())

    
    def send_file(self, file, rem_path):
        file_obj = BytesIO(file.encode())
        self.scp.putfo(file_obj, rem_path)

sshel = SHServer('192.168.0.59', 'user', '123456')

file = open("README.md", 'rb')
sshel.send_file(file.read(), '~/test.txt')