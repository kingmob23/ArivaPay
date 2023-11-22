from app.models.models import User, Admin, Purchase, PromoCode, Transaction


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


def test_new_purchase(session, test_user):
    """
    GIVEN a Purchase model
    WHEN a new Purchase is created
    THEN check the purchase fields are defined correctly
    """
    purchase = Purchase(user_id=test_user.id, total_cost=100.0)
    session.add(purchase)
    session.commit()
    assert purchase in session


def test_new_promocode(session):
    """
    GIVEN a PromoCode model
    WHEN a new PromoCode is created
    THEN check the promocode fields are defined correctly
    """
    promo_code = PromoCode(code="SAVE20", discount_percentage=20.0)
    session.add(promo_code)
    session.commit()
    assert promo_code in session


def test_new_transaction(session, test_user):
    """
    GIVEN a Transaction model
    WHEN a new Transaction is created
    THEN check the transaction fields are defined correctly
    """
    transaction = Transaction(user_id=test_user.id, amount=50.0, transaction_type="deposit")
    session.add(transaction)
    session.commit()
    assert transaction in session
