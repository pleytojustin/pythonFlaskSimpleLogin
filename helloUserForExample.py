from flask import Flask, url_for
#url_for generates urls programatically

app = Flask(__name__)
@app.route("/profile/<username>")
def show_user_profile(username):
    return "User: %s" % username
@app.route("/")
def show_url_for():
    return url_for('show_user_profile', username='jorge')
if __name__ == '__main__':
    app.debug = True
    app.run()
