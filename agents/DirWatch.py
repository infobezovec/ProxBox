import socket
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.connect(("127.0.0.1", 50550))

def send_data(data):
    sock.send(data.encode())
    return data


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return

        print(send_data(f'File {event.src_path} has been modified'))

    def on_created(self, event):
        if event.is_directory:
            return
        print(send_data(f'File {event.src_path} has been created'))

    def on_deleted(self, event):
        if event.is_directory:
            return
        print(send_data(f'File {event.src_path} has been deleted'))

if __name__ == "__main__":
    path = os.getcwd()
    event_handler = MyHandler()
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
