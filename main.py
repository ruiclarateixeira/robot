import sys
sys.path.insert(0, './lib')

import wheels
from time import sleep
from flask import Flask

app = Flask(__name__)
wheels.init()

@app.route("/", methods=['GET'])
def hello():
    return "All systems up!"
    wheels.move_forward()
    sleep(1)
    wheels.stop()

@app.route('/', methods=['POST'])
def execute_order():
    content = request.get_json()
    print content
    return content.type

if __name__ == "__main__":
    app.run()
