#!/usr/bin/env python3

'''
The server.
'''
import socket
import os
import threading

__author__ = 'CS3280'
__version__ = 'Fall 2021'
__pylint__ = 'v1.8.3.'

PORT = 3280

class Server(threading.Thread):
    '''
    Multi-threaded server subclassing Thread.
    '''

    def __init__(self, address):
        super().__init__()
        self.service_threads = []
        self.address = address

    def run(self):
        '''
        Creates a server soket and starts listening.
        '''
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.address))
        server_socket.listen(5)

        while True:
            conn, address = server_socket.accept()
            service_thread = ServiceThread(conn, address, self)
            service_thread.start()
            self.service_threads.append(service_thread)

    def broadcast(self, message, sender_address):
        '''
        Sends a message to all connected clients (except to sender)
        Args: message - the message to send to every connected client.
              sender_address - the address (IP, PORT) of the sender.
        '''
        for service_thread in service_threads:



class ServiceThread(threading.Thread):
    '''
    Thread to service a client.
    '''

    def __init__(self, conn, address, server):
        super().__init__()
        self.conn = conn
        self.address = address
        self.server = server

    def run(self):
        '''
        Receives message from the connected client via socket (conn) and broadcasts the
        message to all other connected clients. If the client has left the connectin
        (ie, no message), the method closes the connected socket and removes ifself (self)
        from the list of service threads of the parent server.
        '''
        #TODO

def handle_bye(server):
    '''
    This method handles program termination.
    '''
    while True:
        command = input('')
        if command == 'bye':
            for service_thread in server.service_threads:
                service_thread.conn.close()
            print('Server is now offline. Good bye!')
            os._exit(0) #pylint: disable=protected-access

def main():
    '''
    Launches the app.
    '''
    address = ('localhost', PORT)
    server = Server(address)
    server.start()

    print('Type \'bye\' at any time to shut down the server...')
    thread = Thread(target=handle_bye)
    thread.start()

if __name__ == '__main__':
    main()
