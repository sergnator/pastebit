import sys

from flask import Flask, request

app = Flask(__name__)


@app.route('/create', methods=['GET'])
def create():
    with open('html//create.html', encoding='utf-8') as f:
        data = f.readlines()
        data = ''.join(data)
    return data.format(request)


@app.route('/', methods=['GET'])
def sample():
    with open('html//main.html', encoding='utf-8') as f:
        data = f.read()
    return data.format(request)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
