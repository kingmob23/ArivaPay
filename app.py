import logging

from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

import toml

with open("config.toml", "r") as f:
    config = toml.load(f)

DB_URL = f"postgresql://{config['db']['user']}:{config['db']['password']}@db:5432/{config['db']['db_name']}"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["FLASK_ADMIN_SWATCH"] = "cerulean"

app.logger.setLevel(logging.INFO)

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)


with app.app_context():
    db.create_all()


@app.route("/")
def index_page():
    return "<p>Main Page</p>"


@app.route("/account")
def account_page():
    return "<p>Personal</p>"


@app.route("/auth")
def auth_page():
    return render_template("auth.html")


admin = Admin(app, name="adminpage", template_mode="bootstrap3")
admin.add_view(ModelView(Dude, db.session))
