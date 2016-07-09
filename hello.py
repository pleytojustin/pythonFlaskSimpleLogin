from flask import Flask, request, render_template, redirect, url_for, flash, session
import logging #for getting logs
from logging.handlers import RotatingFileHandler # appends a nother size when updating the log

#session for session handling
#redirect send to another page
#import function all the data that's pass from the client to the server
#import render_tempalate renders templates that are inside templates
#flash allows passing of messages between URL
app = Flask(__name__)
@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(
            request.form.get('username'),
            request.form.get('password')
        ):

            flash("Succesfully logged in") #used to pass messages between URL
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome'))
        else:
            error = "Incorrect username and password"
            app.logger.warning("Incorrect username and password for user (%s)",
                                request.form.get("username"))
    return render_template('login.html',error=error)
@app.route("/logout")
def logout():
    #stop the session
    session.pop('username', None)
    return redirect(url_for('login'))
@app.route("/")
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('login'))
def valid_login(username, password):
    # checks on the db if the username and password are correct
    if username == password:
        return True
    else:
        return False
if __name__ == '__main__':
    #app secret is used so that we can use flash..
    app.secret_key = "\xe0=\x0f\xba\x8fVN\x1b\x91F2\t\x05\xe2\x94\x91\x97sNB'P\xee\xd8"
    #FOR LOGGING
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    #^FOR LOGGING
    app.debug = True
    app.run()
