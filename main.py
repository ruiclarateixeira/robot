import sys
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/', methods=['POST'])
def add_message():
    content = request.get_json()
    print content
    return content.type;

if __name__ == "__main__":
    app.run()
