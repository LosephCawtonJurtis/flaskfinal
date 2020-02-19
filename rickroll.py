import logging

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home_page():
    return app.send_static_file("index.html")


if __name__ == '__main__':
    app.run(host='10.0.5.12', port=5000, debug=True)