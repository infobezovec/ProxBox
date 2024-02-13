from termcolor import colored
from datetime import datetime

#TESTED
class Logger:
    def __init__(self, logpath="pb.log"):
        self.log_file = open(logpath, 'at')
        pass

    def print_file(self, buffer):
        self.log_file.write(buffer)

    def print_cout(self, buffer, type):
        if type == 'err':
            print(colored(buffer, 'red'))
        elif type == 'warn':
            print(colored(buffer, 'yellow'))
        elif type == 'info':
            print(colored(buffer, 'white'))
        elif type == 'sucs':
            print(colored(buffer, 'green'))

    def ferror(self, message):
        timestamp = datetime.now()
        self.print_file('![ERROR]-|' + str(timestamp.strftime("%Y-%m-%d %H:%M")) + '|- ' + str(message) +'\n')

    def cerror(self, message):
        timestamp = datetime.now()
        self.print_cout('![ERROR]-|' + str(timestamp.strftime("%Y-%m-%d %H:%M")) + '|- ' + str(message) +'\n', 'err')


    def fwarn(self, message):
        timestamp = datetime.now()
        self.print_file('-[WARN ]-|' + str(timestamp.strftime("%Y-%m-%d %H:%M")) + '|- ' + message +'\n')

    def cwarn(self, message):
        timestamp = datetime.now()
        self.print_cout('-[WARN ]-|' + str(timestamp.strftime("%Y-%m-%d %H:%M")) + '|- ' + message +'\n', 'warn')


    def finfo(self, message):
        timestamp = datetime.now()
        self.print_file('*[INFO ]-|' + str(timestamp.strftime("%Y-%m-%d %H:%M")) + '|- ' + message +'\n')

    def cinfo(self, message):
        timestamp = datetime.now()
        self.print_cout('*[INFO ]-|' + str(timestamp.strftime("%Y-%m-%d %H:%M")) + '|- ' + message +'\n', 'info')


    def fsuc(self, message):
        timestamp = datetime.now()
        self.print_file('+[SUCCS]-|' + str(timestamp.strftime("%Y-%m-%d %H:%M")) + '|- ' + message +'\n')

    def csuc(self, message):
        timestamp = datetime.now()
        self.print_cout('+[SUCCS]-|' + str(timestamp.strftime("%Y-%m-%d %H:%M")) + '|- ' + message +'\n', 'sucs')
