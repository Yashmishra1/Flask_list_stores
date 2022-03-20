from flask import Flask

app = Flask(__name__)

@app.route('/')
def Home():
    return "Hello World"

app.run(port=5000)