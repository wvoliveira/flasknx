from flask import Blueprint

bp = Blueprint('common', __name__, url_prefix='/')


@bp.route('/')
def index():
    return 'index'


@bp.route('/ping')
def ping():
    return 'pong'
