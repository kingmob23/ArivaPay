from flask import Flask
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
def index():
    return "<p>Main Page</p>"


admin = Admin(app, name="adminpage", template_mode="bootstrap3")
admin.add_view(ModelView(Dude, db.session))

if __name__ == "__main__":
    app.run()
