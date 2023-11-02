import logging

from flask import Flask, render_template, redirect, url_for
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, UserMixin, login_user, login_required
import toml

from models.models import User, Admin
from models.db_init import init_db

# Load config
with open("config.toml", "r") as f:
    config = toml.load(f)

DB_URL = f"postgresql://{config['db']['user']}:{config['db']['password']}@db:5432/{config['db']['db_name']}"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["FLASK_ADMIN_SWATCH"] = "cerulean"
app.config["SECRET_KEY"] = "your_secret_key"
app.logger.setLevel(logging.INFO)

# Initialize DB
db = init_db(app)

# Flask-Login setup
login_manager = LoginManager(app)
login_manager.login_view = "login"


class MyModelView(ModelView):
    def is_accessible(self):
        # Logic to check if current_user is an admin
        return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("login"))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        # Logic to check if current_user is an admin
        return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("login"))


@app.route("/")
def index_page():
    return """
<p>Main Page</p>
<nav><a href="/">Main Page</a> | <a href="/auth">Auth Page</a></nav><p>Main Page</p>
"""


@app.route("/account")
def account_page():
    return "<p>Personal</p>"


@app.route("/auth")
def auth_page():
    return render_template("auth.html")


@app.route("/login")
def login():
    # Logic to login and validate admin user
    return render_template("login.html")


admin = Admin(
    app, name="adminpage", template_mode="bootstrap3", index_view=MyAdminIndexView()
)
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Admin, db.session))
