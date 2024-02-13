import os
import sys
import time
import socket
import platform

from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



class Watcher(FileSystemEventHandler):
    def __init__(self, ip, port, proto):
        if proto == 'UDP':
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        else:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.sock.connect((ip, int(port)))
        self.init_connect()

    def init_connect(self):
        try:
            path = sys.argv[4]
        except:
            path = os.getcwd()
        user = os.getlogin()
        os_type = platform.system()
        version = platform.version()
        release = platform.release()
        buff = f'I*{path}*{user}*{os_type}*{release}*{version}'
        for i in range(5):
            self.send_data(buff)
            time.sleep(1)
            i+=1
    

    def send_data(self, data):
        self.sock.send(data.encode())
        return data

    def prepare_data(self, mode, filename, type):
        date = datetime.now()
        buff = mode + str(date.strftime("%Y-%m-%d %H:%M")) + '-[' + type +']-' + filename
        return buff

    def on_modified(self, event):
        if event.is_directory:
            return
        self.send_data(self.prepare_data('m', event.src_path, 'MODIFIED'))
        print(f'File {event.src_path} has been modified')

    def on_created(self, event):
        if event.is_directory:
            self.send_data(self.prepare_data('t', event.src_path, 'CRE-DIR'))
            return
        self.send_data(self.prepare_data('c', event.src_path, 'CREATED'))
        print(f'File {event.src_path} has been created')

    def on_deleted(self, event):
        if event.is_directory:
            self.send_data(self.prepare_data('y', event.src_path, 'DEL-DIR'))
            return
        self.send_data(self.prepare_data('d', event.src_path, 'DELETED'))
        print(f'File {event.src_path} has been deleted')


def print_help():
    print("""
EXAMPLE: IEObserver.exe 10.0.10.1 434 UDP C:\\Users\\User\\Desktop
          
arg 1 - Server IP
arg 2 - Server PORT
arg 3 - TCP or UDP 
arg 4 - Directory to watch if none - watch current directory
          """)


def main():
    if len(sys.argv) <= 3:
        print_help()
        exit()
    event_handler = Watcher(sys.argv[1], sys.argv[2], sys.argv[3])

    if len(sys.argv) < 4:
        path = sys.argv[4]
    else:
        path = os.getcwd()

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    print(f"Watching directory {path} for changes...")

    try:
        observer.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()



if __name__ == "__main__":
    main()
