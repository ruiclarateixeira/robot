from time import sleep
import SocketServer
import wheels
from SimpleWebSocketServer import WebSocket


class MyWebSocket(WebSocket):
    def handle_command(self, data):
        func = {
            'w': wheels.move_forward,
            's': wheels.move_backward,
            'a': wheels.turn_left,
            'd': wheels.turn_right,
            'p': wheels.stop
        }.get(data, None)

        if func is not None:
            func()

    def handleMessage(self):
        self.handle_command(self.data)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')
