from flask import Flask, render_template, session
from flask import request
import json
import random


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/home.html")
def home():
    return render_template('index.html')

@app.route("/index.html", methods=['POST'])
def get_mail():
    email = request.form['Email']
    print(email.split('@')[0])
    return "Success"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)