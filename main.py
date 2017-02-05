import sys
sys.path.insert(0, './lib')

import signal
import SocketServer
from time import sleep
from flask import Flask
from sys import platform
from tcphandler import MyTCPHandler
from threading import Thread

if platform != "darwin":
    import wheels
    wheels.init()

app = Flask(__name__)

@app.route("/testflask")
def test_flask():
    return "Flask is working!"

@app.route("/", methods=['GET'])
def hello():
    return wheels.diagnostic()

@app.route('/', methods=['POST'])
def execute_order():
    content = request.get_json()
    print content
    return content.type

def start_flask():
    FLASK_URL, FLASK_PORT = "0.0.0.0", 5000
    print "Starting flask server on {}:{}".format(FLASK_URL, FLASK_PORT)
    app.run(host=FLASK_URL, port=FLASK_PORT)

def start_tcp_listener():
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

    flask_thread = Thread(target=start_flask)
    flask_thread.start()

    tcp_thread = Thread(target=start_tcp_listener)
    tcp_thread.start()

    sleep(1)
    while(True):
        var = raw_input("Ctrl+C to Stop")
