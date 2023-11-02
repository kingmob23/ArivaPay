from models import db

def init_db(app):
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # db.init_app(app)
    return db
