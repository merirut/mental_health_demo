from flask import Flask, render_template

from . import __name__

flask_app = Flask(__name__)

@flask_app.route('/')
def main():
    return render_template("index.html")

@flask_app.route('/other')
def other():
    return render_template("index.html")