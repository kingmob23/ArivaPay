from flask import render_template
from . import auth


@auth.route("/login")
def login():
    return "<p>Login Page</p>"


@auth.route("/auth")
def auth_page():
    return render_template("auth.html")
