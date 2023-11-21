import os
import toml
from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

from .admin.views import MyAdminIndexView, MyModelView
from .models import User, Admin as AdminModel
from .api.promocodes import promocodes_blueprint
from .api.purchases import purchases_blueprint
from .auth import auth as auth_blueprint
from .main import main as main_blueprint

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        # Load the default configuration
        base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        config_path = os.path.join(base_dir, "app", "config.toml")
        with open(config_path, "r") as f:
            config = toml.load(f)
        db_url = f"postgresql://{config['db']['user']}:{config['db']['password']}@db:5432/{config['db']['db_name']}"
        app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    else:
        # Load the testing configuration passed to the function
        app.config.update(test_config)

    app.config["FLASK_ADMIN_SWATCH"] = "cerulean"
    app.config["SECRET_KEY"] = "your_secret_key"

    db.init_app(app)

    admin = Admin(app, name="adminpage", template_mode="bootstrap3", index_view=MyAdminIndexView())
    admin.add_view(MyModelView(User, db.session))
    admin.add_view(MyModelView(AdminModel, db.session, endpoint="adminmodel"))

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(purchases_blueprint)
    app.register_blueprint(promocodes_blueprint)

    @app.cli.command("init_db")
    def init_db_command():
        """Create database tables from SQLAlchemy models."""
        db.create_all()
        print("Initialized the database.")

    return app
