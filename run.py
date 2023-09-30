from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import inspect
from app.models import User
import logging

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@db:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["FLASK_ADMIN_SWATCH"] = "cerulean"

app.logger.setLevel(logging.INFO)

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

with app.app_context():
    inspector = inspect(db.engine)
    table_names = inspector.get_table_names()

# Check if 'user' table is in the list of table names
if "user" in table_names:
    print("The 'user' table was successfully created.")
else:
    print("The 'user' table was not found in the database.")

admin = Admin(app, name="adminpage", template_mode="bootstrap3")
admin.add_view(ModelView(User, db.session))

if __name__ == "__main__":
    app.run()
