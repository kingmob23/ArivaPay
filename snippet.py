import os
import os.path as op
from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.event import listens_for
from flask.ext.security import (
    current_user,
    login_required,
    RoleMixin,
    Security,
    SQLAlchemyUserDatastore,
    UserMixin,
)
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib import sqla

# Create application
app = Flask(__name__)

# Create dummy secrety key so we can use sessions
app.config["SECRET_KEY"] = "123456790"

# Create in-memory database
app.config["DATABASE_FILE"] = "sample_db.sqlite"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + app.config["DATABASE_FILE"]
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

# Create directory for file fields to use
file_path = op.join(op.dirname(__file__), "static/files")

# flask-security models

roles_users = db.Table(
    "roles_users",
    db.Column("user_id", db.Integer(), db.ForeignKey("user.id")),
    db.Column("role_id", db.Integer(), db.ForeignKey("role.id")),
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship(
        "Role", secondary=roles_users, backref=db.backref("users", lazy="dynamic")
    )


# Create Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Only needed on first execution to create first user
# @app.before_first_request
# def create_user():
#    db.create_all()
#    user_datastore.create_user(email='yourmail@mail.com', password='pass')
#    db.session.commit()


class AnyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))

    def __unicode__(self):
        return self.name


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return (
            current_user.is_authenticated()
        )  # This does the trick rendering the view only if the user is authenticated


# Create admin. In this block you pass your custom admin index view to your admin area
admin = Admin(
    app, "Admin Area", template_mode="bootstrap3", index_view=MyAdminIndexView()
)


# Add views
admin.add_view(sqla.ModelView(AnyModel, db.session))


# To acess the logout just type the route /logout on browser. That redirects you to the index
@login_required
@app.route("/login")
def login():
    return redirect("/admin")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # Build sample db on the fly, if one does not exist yet.
    db.create_all()
    app.run(debug=True)
