from flask import Blueprint, jsonify

from app.models.models import Purchase

purchases_blueprint = Blueprint("purchases", __name__)


@purchases_blueprint.route("/api/purchases/<int:user_id>", methods=["GET"])
def get_purchases(user_id):
    purchases = Purchase.query.filter_by(user_id=user_id).all()
    return jsonify([purchase.to_dict() for purchase in purchases])
