import os
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/python')
def hello_world():
    return 'Flask Dockerized'
@app.route('/python/test')
def hello_world2():
    return 'python route extended!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')