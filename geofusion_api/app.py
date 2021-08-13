from flask import Flask
from geofusion_api import config, db, api, cli


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    api.init_app(app)

    return app
