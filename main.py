import sys
sys.path.insert(0, './lib')

import signal
import SocketServer
import os
import wheels
from sys import platform, argv
from tcphandler import MyWebSocket
from SimpleWebSocketServer import SimpleWebSocketServer
wheels.init()


def start_web_socket():
    if len(argv) > 1:
        TCP_HOST, TCP_PORT = argv[1], 5001
    else:
        TCP_HOST, TCP_PORT = "localhost", 5001

    server = SimpleWebSocketServer(TCP_HOST, TCP_PORT, MyWebSocket)
    server.serveforever()


def sigint_handler(signum, frame):
    print "Exiting"
    sys.exit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler)
    print "Running on {}".format(platform)
    print "Process id {}".format(os.getpid())

    start_web_socket()
