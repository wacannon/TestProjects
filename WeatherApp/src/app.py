from flask import Flask, render_template, request, session
from openweatherapi import getdailyforecast
import sys, datetime


reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'why would I tell you my secret key?'


@app.route("/")
def main():
    data = getdailyforecast()
    return render_template('index.html', data=data)


@app.template_filter('shortdate')
def _jinja2_filter_datetime(date):
    shortdate = datetime.datetime.fromtimestamp(int(date)).strftime('%m-%d')
    return shortdate

if __name__ == "__main__":
    app.run()
