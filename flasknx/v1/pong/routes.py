from flask import Blueprint

bp = Blueprint('v1_pong', __name__, url_prefix='/v1/pong')


@bp.route('/')
def index():
    return '/v1/pong index'
