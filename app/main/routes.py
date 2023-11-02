from . import main


@main.route("/")
def index_page():
    return "<p>Main Page</p>"


@main.route("/account")
def account_page():
    return "<p>Personal Account</p>"
