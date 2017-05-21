import SocketServer

def temp_move():
    print "Executing!"

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle_command(self, data):
        func = {
            'f': temp_move,
            'b': temp_move,
            'r': temp_move,
            'l': temp_move,
        }.get(data, None)

        if func is not None:
            func()

    def handle(self):
        while(True):
            self.handle_command(self.request.recv(1).strip())