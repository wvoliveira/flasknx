import os

from flask import Flask
from flasknx.common.metrics import metrics

__app__ = 'flasknx'
__info__ = 'just a example with flask + uwsgi + nginx'
__version__ = '0.0.1'


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=os.urandom(10)
    )

    if test_config is not None:
        app.config.update(test_config)

    from flasknx.common import routes, healthcheck
    from flasknx.v1.ping import routes as v1_ping
    from flasknx.v1.pong import routes as v1_pong

    app.register_blueprint(healthcheck.bp)
    app.register_blueprint(routes.bp)
    app.register_blueprint(v1_ping.bp)
    app.register_blueprint(v1_pong.bp)

    metrics.init_app(app)

    return app
