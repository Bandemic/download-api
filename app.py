from flask import Flask, escape, request, jsonify, Response, abort
from datetime import datetime
from db import mongo, get_cases, insert_random_cases
import dateutil.parser as dateparser
from uuid import UUID
from typing import Union, Optional
import os

app = Flask(__name__, instance_relative_config=True)
env = os.environ.get("FLASK_ENV", "production")
if env == "production":
    app.config.from_object("config.ProductionConfig")
elif env == "development":
    app.config.from_object("config.DevelopmentConfig")
elif env == "testing":
    app.config.from_object("config.TestingConfig")


app.config["APPLICATION_ROOT"] = "/"

mongo.init_app(app)

# TODO: instead of a timestamp passing a single UUID might be better here
@app.route("/v1/cases")
def cases():
    lat: Union[Optional[float], int] = request.args.get("lat", type=float)
    lon: Union[Optional[float], int] = request.args.get("lon", type=float)
    uuid: Optional[UUID] = request.args.get("uuid", type=UUID)
    if uuid is None:
        return Response("Please pass a uuid", status=400)

    try:
        if lat is not None:
            lat = round(lat)
        if lon is not None:
            lon = round(lon)
    except ValueError:
        abort(400)

    cases = get_cases(uuid, lat=lat, lon=lon)

    def generate():
        for case in cases:
            uuid = str(case["uuid"])
            yield uuid + ","

    return Response(generate(), mimetype="application/octet-stream")


issubclass


@app.route("/v1/insert/<int:n>")
def insert(n):
    if not app.config["DEBUG"]:
        abort(404)
    insert_random_cases(n)
    return Response("Successfully inserted {:d} random cases".format(n), status=200)
