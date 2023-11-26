import json
import os

from flask import Flask, request, url_for, render_template

app = Flask(__name__)


@app.route('/create', methods=['GET'])
def create():
    return render_template('create.html')


@app.route(rule='/NewPost', methods=['POST'])
def new_post():
    json_data = str(request.data)
    json_data = json_data.split("'")[1]
    json_data = json.loads(json_data)
    id = generate_id()
    with open(f'storage/{id}.txt', mode='w') as f:
        f.write(json_data['text'])
    url = generate_url(id)

    return url


@app.route("/storage/getpost")
def get_post():
    id = request.args.get('id')
    with open(f'storage/{id}.txt', encoding='utf-8') as f:
        data = f.read()
    return data.format(request)


@app.route('/', methods=['GET'])
def sample():
    return render_template('main.html')


def generate_id():
    listdir = os.listdir('storage')
    listdir = map(lambda x: x.split('.')[0], listdir)
    listdir = list(map(int, listdir))
    if len(listdir) == 0:
        return '1'
    return str(max(listdir) + 1)


def generate_url(id: str):
    return f"storage/getpost?id={id}"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
