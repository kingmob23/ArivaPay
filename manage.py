from flask_script import Manager
from app import create_app, db

app = create_app()
manager = Manager(app)

@manager.command
def init_db():
    """Create database tables from sqlalchemy models."""
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    manager.run()
