"""
Sockets for cross-task communication: start threads to communicate over sockets.
Independent programs can too, because sockets are system-wide, much like fifos.
Some socket servers may also need to talk to clients in threads or processes.
Sockets pass byte strings, but can be pickled objects or encoded Unicode text.
Caveat: prints in threads may need to be synchronized if their output overlaps.
"""

from socket import socket, AF_INET, SOCK_STREAM

port = 50007
host = 'localhost'


def server():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)
    while True:
        connection, addr = sock.accept()
        data = connection.recv(1024)
        reply = f'Server got {data}'
        connection.send(reply.encode())


def client(name):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send(name.encode())
    reply = sock.recv(1024)
    sock.close()
    print(f'Client got {reply}')


if __name__ == '__main__':
    from threading import Thread
    server_thread = Thread(target=server)
    server_thread.daemon = True
    # Don't wait for server thread.
    server_thread.start()
    # Do wait for children to exit.
    for i in range(5):
        Thread(target=client, args=(f'client{i}',)).start()
