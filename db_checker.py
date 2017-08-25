from __future__ import print_function
from pymongo import MongoClient
from datetime import datetime
import threading
import time

client = MongoClient()
db = client.ttyl
ttyl_local = db.ttyl_local_collection


def loop_db():
    while True:
        for doc in ttyl_local.find():
            pass
            curr_time = datetime.now()
            # 0001-02-01T02:03
            # year-month-dayThour:minute
            doc_time = datetime.strptime(doc['date'].replace('T',' '), '%Y-%m-%d %H:%M')
            # datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
            if same_minute(curr_time, doc_time):
                send_text(doc)
        time.sleep(30)


def db_checker():
    t = threading.Thread(target=loop_db)
    t.start()


def same_minute(curr_time, doc_time):
    return (curr_time.year == doc_time.year and
            curr_time.month == doc_time.month and
            curr_time.day == doc_time.day and
            curr_time.hour == doc_time.hour and
            curr_time.minute == doc_time.minute)
