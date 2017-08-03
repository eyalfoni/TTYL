from __future__ import print_function
from flask import Flask, url_for, render_template, request
import sys
app = Flask(__name__)

# This main page is a welcome page
# The user click a button and enters
# the main page


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/ttyl', methods=['GET', 'POST'])
def main_page():
    if request.method == 'GET':
        return render_template('main_page.html')
    elif request.method == 'POST':
        user_num = request.form['user_num']
        sending_num = request.form['sending_num']
        return user_num + ' ' + sending_num
    else:
        return 'What\'s going on?'


def schedule_text():
    pass
