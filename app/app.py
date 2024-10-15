from flask import Flask
from app import api
from app.extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")

    configure_extensions(app)
    register_blueprints(app)

    return app


def configure_extensions(app):
    db.init_app(app)


def register_blueprints(app):
    app.register_blueprint(api.views.blueprint)
