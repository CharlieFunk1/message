from flask import Flask, render_template, url_for, request, session, redirect
import datetime
from database.messagedef import Message, User, database

app = Flask(__name__, static_folder='static',template_folder="templates",static_url_path='')


@app.route('/signupdata', methods=['GET','POST'])
def signupdata():
    if request.method == "POST":
        newuname = req.form["newuname"]
        newpword = req.form["newpword"]
        newemail = req.form["newemail"]
        if newuname != "" and newpword != "" and newemail != "":
            user = User(newuname, newpword, newfname)
            database.add(user)
            database.commit()
            return render_template('signupcomplete.html', uname = newuname)
        else:
            return render_template('signup.html',message = "Invalid information.  Please try again.")
    else:
        return render_template('signup.html',message = "Invalid information.  Please try again.")
if __name__ == '__main__':
    app.run(threaded=True, port=5000, debug=True)
