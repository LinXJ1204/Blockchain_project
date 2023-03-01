from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html")


if __name__ == '__main__':
    app.debug = True
    app.run()