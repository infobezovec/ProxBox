import os
import paramiko
import tempfile
from io import BytesIO
from scp import SCPClient
from PBLogger import Logger

#TESTED
class SHServer:
    def __init__(self, host, username, pswd):
        self.host = host
        self.log = Logger()
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self.ssh.connect(host, 22, username, pswd)
            self.scp = SCPClient(self.ssh.get_transport())
            self.log.finfo("SSH/SCP - Connected")
        except:
            err = 'SSH/SCP Connection error'
            self.log.cerror(err)
            self.log.ferror(err)
            exit()
    
    def cmd_exec(self, cmd):
        try:
            stdin, stdout, stderr = self.ssh.exec_command(cmd)
            self.log.finfo('EXECUTED-[' + self.host + ']:' + cmd)
        except:
            self.log.ferror(Exception)
        for line in stdout:
            print(line.strip())

    def send_data(self, data, rem_path):
        file_obj = BytesIO(data)
        try:
            self.scp.putfo(file_obj, rem_path)
            self.log.fsuc('LOADED DATA-[' + self.host + ']:' + rem_path)
        except:    
            err = 'SSH/SCP Send data error'
            self.log.cerror(err)
            self.log.ferror(err)

    def send_file(self, file, rem_path):
        try:
            self.scp.put(file, rem_path)
            self.log.fsuc('LOADED FILE-[' + self.host + ']:' + file + ' -TO-> ' + rem_path)
        except:
            err = 'SSH/SCP Send file error'
            self.log.cerror(err)
            self.log.ferror(err)

    def download_file(self, rem_path, local_path):
        try:
            self.scp.get(rem_path, local_path + '.dwnl')
            self.log.fsuc('DOWNLOADED FILE-[' + self.host + ']:' + rem_path + ' -TO-> ' + local_path + '.dwnl')
        except:
            err = 'SSH/SCP Download error'
            self.log.cerror(err)
            self.log.ferror(err)


sshel = SHServer('192.168.100.9', 'user', '123456')
#sshel.cmd_exec('ls')
file = open("pb.log", 'rb')
b = file.read()
sshel.send_file('Sandbox.py', '~/test2.txt')
#sshel.cmd_exec('ls')
sshel.download_file("~/test2.txt", "downloaded.txt")