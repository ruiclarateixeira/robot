import sys
sys.path.insert(0, './lib')

import signal
import SocketServer
import os
from time import sleep
from sys import platform, argv
from tcphandler import MyTCPHandler
from threading import Thread
import wheels

wheels.init()

def start_tcp_listener():
    if len(argv) > 1:
        TCP_HOST, TCP_PORT = argv[1], 5001
    else:
        TCP_HOST, TCP_PORT = "localhost", 5001
        
    print "Starting TCP socket on {}:{}".format(TCP_HOST, TCP_PORT)
    server = SocketServer.TCPServer((TCP_HOST, TCP_PORT), MyTCPHandler)
    server.serve_forever()

def sigint_handler(signum, frame):
    print "Exiting"
    sys.exit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler)
    print "Running on {}".format(platform)
    print "Process id {}".format(os.getpid())

    tcp_thread = Thread(target=start_tcp_listener)
    tcp_thread.start()
