from flask import Blueprint, request, Response, abort, current_app
from uuid import UUID
from typing import Union, Optional, Generator
from app.persistence.db import get_cases, insert_random_cases
from app.model import ApiError

cases = Blueprint("v0.cases", __name__, url_prefix="/v0/cases")


@cases.route("", methods=["GET"], strict_slashes=False)
def index() -> Response:
    lat: Union[Optional[float], int] = request.args.get("lat", type=float)
    lon: Union[Optional[float], int] = request.args.get("lon", type=float)
    uuid: Optional[UUID] = request.args.get("uuid", type=UUID)

    if uuid is None:
        return ApiError(400, "No valid UUID for the requested query").as_response()

    try:
        if lat is not None:
            lat = round(lat)
        if lon is not None:
            lon = round(lon)
    except ValueError:
        abort(400)

    cases = get_cases(uuid, lat=lat, lon=lon)

    def generate() -> Generator[str, None, None]:
        for case in cases:
            case_uuid = str(case["uuid"])
            yield case_uuid + ","

    return Response(generate(), mimetype="application/octet-stream")


@cases.route("/insert/<int:n>", methods=["POST"])
def insert(n: int) -> Response:
    if not current_app.config["DEBUG"]:
        return ApiError(501, "Only available for debugging.").as_response()
    insert_random_cases(n)
    return Response("Successfully inserted {:d} random cases".format(n), status=201)
