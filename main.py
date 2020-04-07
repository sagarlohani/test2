from flask import Flask, render_template, session
from flask import request
import json
import random


app = Flask(__name__)


@app.route("/home.html")
def home():
    return render_template('index.html')


@app.route("/index.html", methods=['POST'])
def get_mail():
    email = request.form['Email']
    username = email.split('@')[0]
    call_ansible(username)
    return "Success"


def call_ansible(username):
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('52.77.220.46', username='cloud_user', password='Pwcwelcome1!')
    stdin, stdout, stderr = client.exec_command('echo' + " " + username)
    for line in stdout:
        print('... ' + line.strip('\n'))
    client.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)