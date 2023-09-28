from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, login_required
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key_here"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///your_database.db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define your User and Role models
from flask_security import UserMixin, RoleMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship(
        "Role", secondary="roles_users", backref=db.backref("users", lazy="dynamic")
    )


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


# Define the association table for User and Role
roles_users = db.Table(
    "roles_users",
    db.Column("user_id", db.Integer(), db.ForeignKey("user.id")),
    db.Column("role_id", db.Integer(), db.ForeignKey("role.id")),
)

# Create Flask-Security datastore
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# Routes
@app.route("/")
def hello_world():
    return "<p>MAIN PAGE</p>"


@app.route("/admin")
@login_required
def admin_panel():
    return "<p>ADMIN PANEL</p>"
