from __future__ import print_function
from flask import Flask, url_for, render_template, request
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient()
db = client.ttyl
ttyl_local = db.ttyl_local_collection

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
        date = request.form['date']
        msg = request.form['msg']

        # add document to db
        ttyl_local_document = {'user_num': user_num,
                               'sending_num': sending_num,
                               'date': date,
                               'msg': msg
                               }
        ttyl_local.insert(ttyl_local_document)

        return render_template('submit.html', user_num=user_num,
                               sending_num=sending_num, date=date, msg=msg)
    else:
        return 'What\'s going on?'


def schedule_text():
    pass
