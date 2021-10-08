from flask import Flask, render_template, url_for, request, session, redirect
import datetime
from tables.messagedef import Message, User, database


app = Flask(__name__, static_folder='static',template_folder="templates",static_url_path='')


@app.route('/')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(threaded=True, port=5000, debug=True)
