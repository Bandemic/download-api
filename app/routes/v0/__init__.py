from flask import Blueprint, escape, request, jsonify, Response, abort, current_app
from datetime import datetime
import dateutil.parser as dateparser
from uuid import UUID
from typing import Union, Optional
import os
from db import get_cases, insert_random_cases

cases = Blueprint("v0.cases", __name__, url_prefix="/v0/cases")


@cases.route("", methods=["GET"])
def index() -> Response:
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
            case_uuid = str(case["uuid"])
            yield case_uuid + ","

    return Response(generate(), mimetype="application/octet-stream")


@cases.route("/insert/<int:n>", methods=["POST"])
def insert(n) -> Response:
    if not current_app.config["DEBUG"]:
        abort(404)
    insert_random_cases(n)
    return Response("Successfully inserted {:d} random cases".format(n), status=201)
