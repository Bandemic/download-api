from flask import Flask
from db import db
import config
import os

from .routes.v0 import cases


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(cases)
    env = os.environ.get("FLASK_ENV", "production")
    if env == "production":
        app.config.from_object("config.ProductionConfig")
    elif env == "development":
        app.config.from_object("config.DevelopmentConfig")
    elif env == "testing":
        app.config.from_object("config.TestingConfig")
        mongo_uri = os.environ.get("MONGO_URI")
        if mongo_uri is not None:
            app.config.update({"MONGO_URI": mongo_uri})

    db.init_app(app)
    return app
