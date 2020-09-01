# app.py
from flask import Flask

app = Flask('app')


@app.route('/')
def index():
    return "I'm from docker"


if __name__ == '__main__':
    print('reach1')
    app.run(host='127.0.0.1',port=8080, debug=True)
else:
    print('imported')