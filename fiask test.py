from flask import Flask
from markupsafe import escape
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Welcome to Paradise!"
@app.route("/Start")
def hi_world():
    return "Lets get started?"
@app.route("/user/<username>")
def user(username):
    return "Welcome user: %s" % escape(username)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)