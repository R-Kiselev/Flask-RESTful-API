from flask import Flask

from app import api
from app.extensions import db, migrate
from app.api.error_handling import register_api_errorhandlers

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")

    configure_extensions(app)
    register_blueprints(app)

    return app

def configure_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)

def register_blueprints(app):
    register_api_errorhandlers(api.views.blueprint)
    app.register_blueprint(api.views.blueprint)
