from flask import Flask, url_for, render_template
app = Flask(__name__)

# This main page is a welcome page
# The user click a button and enters
# the main page


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/ttyl', methods=['GET', 'POST'])
def main_page():
    return 'fml'
