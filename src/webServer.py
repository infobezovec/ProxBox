import socket
from termcolor import colored
#TODO write remote module stop
class SBServer:
    def __init__(self, bind_addr, port, proto):
        if proto == 'UDP':
            self.input_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        else:
            self.input_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.input_socket.bind((bind_addr, int(port)))
        self.init_connect()

    def init_connect(self):
        print("WAITING FOR CONNECTION")
        buff = ''
        while True:
            buff, addr = self.input_socket.recvfrom(512)
            buff = buff.decode()
            if buff[0] == "I":
                buff = buff[1:]
                data = buff.split('*')
                if len(data) == 6:
                    print(colored("CONNECTED AGENT AT: " + str(addr[0]) + ' - '+ data[3] +  data[4] + ' - RELEASE: ' + data[5] , 'green'))
                break    
        return buff

    def listen(self, size=1024):
        print("Listen ")
        while True:
            buff, addr = self.input_socket.recvfrom(size)
            if len(buff) > 1:
                decoded = buff.decode()
                mode = decoded[0]
                decoded = decoded[1:]
                if mode == 'm':
                    print(colored("Recieved: " + decoded + "\tfrom: ", 'blue'))
                elif mode == 't':
                    print(colored("Recieved: " + decoded + "\tfrom: ", 'green'))
                elif mode == 'c':
                    print(colored("Recieved: " + decoded + "\tfrom: ", 'green'))
                elif mode == 'y':
                    print(colored("Recieved: " + decoded + "\tfrom: ", 'red'))
                elif mode == 'd':
                    print(colored("Recieved: " + decoded + "\tfrom: ", 'red'))
        client.close
        input_socket.close

#TEST
def main():
    serv = SBServer('192.168.0.76', 800, 'UDP')
    serv.listen()



main()