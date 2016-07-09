from flask import Flask, request
#import function all the data that's pass from the client to the server

app = Flask(__name__)
@app.route("/login", methods=['GET'])
def login(username):
    if request.values:
        return 'username is %s' % request.values['username']
    else:
        return '<form method="get" action="/login"><input type="text" name="username"/><p><button type="submit">Submit</button>'
if __name__ == '__main__':
    app.debug = True
    app.run()
