import pytest
from sqlalchemy.orm import sessionmaker, scoped_session

from app import create_app
from app.models import db as _db, User, Admin


@pytest.fixture(scope="module")
def test_app():
    """
    Create a Flask application context for the tests.
    """
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    }
    app = create_app(test_config)

    # Flask context and database setup
    with app.app_context():
        _db.create_all()
        yield app  # testing happens here
        _db.session.remove()
        _db.drop_all()


@pytest.fixture(scope="function")
def session(test_app):
    """
    Create a new database session for a test.
    """
    connection = _db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})

    session_factory = sessionmaker(bind=connection)
    session = scoped_session(session_factory)

    _db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()
