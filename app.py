from flask import Flask, request, url_for, render_template

app = Flask(__name__)


@app.route('/create', methods=['GET'])
def create():
    return render_template('create.html')


def new_post():
    pass


@app.route('/', methods=['GET'])
def sample():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
