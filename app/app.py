from flask import Flask
import os

app = Flask(__name__)


print('Starting server')
@app.route('/ping')
def ping():
    return "ok"



@app.route('/kill-program')
def fail():
    os._exit(12)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
