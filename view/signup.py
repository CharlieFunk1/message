from flask import Flask, render_template, url_for, request, session, redirect
import datetime
from database.messagedef import Message, User, database
from view.signupdata import signupdata

app = Flask(__name__, static_folder='static',template_folder="templates",static_url_path='')


@app.route('/signup', methods=['GET','POST'])
def signup():
    return render_template('signup.html', message="Please create an account to post or reply to messages")

if __name__ == '__main__':
    app.run(threaded=True, port=5000, debug=True)
