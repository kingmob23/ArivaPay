from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from .. import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    referral_code = db.Column(
        db.String(64), unique=True
    )  # Добавлено для реферальной программы
    referred_by = db.Column(db.String(64))  # Кто пригласил пользователя


class Admin(db.Model):
    __tablename__ = "admins"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)


class Purchase(db.Model):
    __tablename__ = "purchases"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    purchase_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_cost = db.Column(db.Float)
    # Можно добавить дополнительные поля, например, список товаров


class PromoCode(db.Model):
    __tablename__ = "promocodes"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(64), unique=True)
    discount_percentage = db.Column(db.Float)
    valid_until = db.Column(db.DateTime)
    # Дополнительные поля для ограничений использования промокодов


class Transaction(db.Model):
    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    transaction_date = db.Column(db.DateTime, default=datetime.utcnow)
    amount = db.Column(db.Float)
    transaction_type = db.Column(db.String(64))  # Например, "deposit", "withdrawal"
