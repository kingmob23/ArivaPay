import pytest
from app.models import User, Admin


def test_new_user(session):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the username fields are defined correctly
    """
    user = User(username="test_user")
    session.add(user)
    session.commit()
    assert user in session


def test_new_admin(session):
    """
    GIVEN an Admin model
    WHEN a new Admin is created
    THEN check the username and password fields are defined correctly
    """
    admin = Admin(username="admin_user", password="secure_password")
    session.add(admin)
    session.commit()
    assert admin in session
