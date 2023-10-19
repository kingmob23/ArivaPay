from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
import logging

DB_URL = "postgresql://user:password@db:5432/postgres"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["FLASK_ADMIN_SWATCH"] = "cerulean"

app.logger.setLevel(logging.INFO)


db = SQLAlchemy(app)


class Dude(db.Model):
    __tablename__ = "dude"

    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return self.id


def create_tables():
    with app.app_context():
        if not Dude.__table__.exists(bind=db.engine):
            db.create_all()


@app.route("/")
def inde_page():
    return "<p>Main Page</p>"


@app.route("/account")
def account_apge():
    return "<p>ЛичКаб</p>"


@app.route("/auth")
def auth_page():
    return render_template("auth.html")


admin = Admin(app, name="adminpage", template_mode="bootstrap3")
admin.add_view(ModelView(Dude, db.session))

if __name__ == "__main__":
    app.run()
