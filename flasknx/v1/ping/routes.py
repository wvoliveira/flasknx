from flask import Blueprint

bp = Blueprint('v1_ping', __name__, url_prefix='/v1/ping')


@bp.route('/')
def index():
    return '/v1/ping index'
