from flask import Blueprint, jsonify

from .models import PromoCode

promocodes_blueprint = Blueprint("promocodes", __name__)


@promocodes_blueprint.route("/api/promocodes", methods=["GET"])
def get_promocodes():
    promocodes = PromoCode.query.all()
    return jsonify([promocode.to_dict() for promocode in promocodes])
