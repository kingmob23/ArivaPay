from . import main
from app.auth import auth_page


@main.route("/")
def index_page():
    return "<p>Main Page</p>"

@main.route("/account")
def account_page():
    return "<p>Personal Account</p>"

@main.route("/auth")
def auth_page_proxy():
    return auth_page()