from flask import Flask
from .models import db
from flask_admin import User, Admin
from .admin.views import MyModelView, MyAdminIndexView
import toml


def create_app():
    app = Flask(__name__)

    # Load config
    with open("config.toml", "r") as f:
        config = toml.load(f)

    DB_URL = f"postgresql://{config['db']['user']}:{config['db']['password']}@db:5432/{config['db']['db_name']}"
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
    app.config["FLASK_ADMIN_SWATCH"] = "cerulean"
    app.config["SECRET_KEY"] = "your_secret_key"

    db.init_app(app)

    # Set up Flask-Admin
    admin = Admin(
        app, name="adminpage", template_mode="bootstrap3", index_view=MyAdminIndexView()
    )
    admin.add_view(MyModelView(User, db.session))
    admin.add_view(MyModelView(Admin, db.session))

    from app.main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from app.auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    return app
