from flask import Flask, render_template, request, session

import sys, dateutil


reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'why would I tell you my secret key?'

@app.route("/")
def main():
    data = dayforcast()
    return render_template('index.html', data=data)
