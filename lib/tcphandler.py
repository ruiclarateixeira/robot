from time import sleep
import SocketServer
import wheels

def step_forward():
    wheels.move_forward()
    sleep(0.5)
    wheels.stop()

def step_backwards():
    wheels.move_backward()
    sleep(0.5)
    wheels.stop()

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle_command(self, data):
        func = {
            'w': step_forward,
            's': step_backwards,
            'a': wheels.stop,
            'd': wheels.stop,
            'p': wheels.stop
        }.get(data, None)

        if func is not None:
            func()

    def handle(self):
        while(True):
            self.handle_command(self.request.recv(1).strip())
