import socket

class SBServer:

    def server_():
        input_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        input_socket.bind(('127.0.0.1', 50550))

        print("Listen")
        while True:
            buff, addr = input_socket.recvfrom(512)
            print("Recieved: ", buff.decode(), "\tfrom: ", addr)

        client.close
        input_socket.close