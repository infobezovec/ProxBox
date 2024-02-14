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
            self.log.werror(err)
            exit()
    
    def cmd_exec(self, cmd):
        try:
            stdin, stdout, stderr = self.ssh.exec_command(cmd)
            self.log.finfo('EXECUTED-[' + self.host + ']:' + cmd + '[RESULT]: ' + str(stdout))
        except:
            self.log.werror("EXECUTE ERROR" + str(stderr))
            
        for line in stdout:
            print(line.strip())
        return stderr

    def send_data(self, data, rem_path):
        file_obj = BytesIO(data)
        try:
            self.scp.putfo(file_obj, rem_path)
            self.log.fsuc('LOADED DATA-[' + self.host + ']:' + rem_path)
        except:    
            err = 'SSH/SCP Send data error'
            self.log.werror(err)

    def send_file(self, file, rem_path):
        try:
            self.scp.put(file, rem_path)
            self.log.fsuc('LOADED FILE-[' + self.host + ']:' + file + ' -TO-> ' + rem_path)
        except:
            err = 'SSH/SCP Send file error'
            self.log.werror(err)

    def download_file(self, rem_path, local_path):
        try:
            self.scp.get(rem_path, local_path + '.dwnl')
            self.log.fsuc('DOWNLOADED FILE-[' + self.host + ']:' + rem_path + ' -TO-> ' + local_path + '.dwnl')
        except:
            err = 'SSH/SCP Download error'
            self.log.werror(err)


    def run_file(self, rem_path, args):
        self.cmd_exec(f'./{rem_path} {args}')
        pass

    def shut_sys(self, timeout=10):
        self.cmd_exec(f"shutdown /s /t {timeout}")

sshel = SHServer('192.168.0.66', 'Maksim', '123456')
sshel.shut_sys(15)