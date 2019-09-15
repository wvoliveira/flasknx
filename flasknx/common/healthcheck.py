from flask import Blueprint
from healthcheck import HealthCheck

bp = Blueprint('healthcheck', __name__)
health = HealthCheck()


def x_dependencie():
    check = True
    return check, 'X dependencie OK'

health.add_check(x_dependencie)

bp.add_url_rule('/healthcheck', 'healthcheck', view_func=lambda: health.run())
