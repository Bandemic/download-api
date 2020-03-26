from flask import Flask, escape, request, jsonify, Response
import dateutil.parser as dateparser
import datetime

from db import get_cases

app = Flask(__name__)

app.config["APPLICATION_ROOT"] = "/"


# TODO: instead of a timestamp passing a single UUID might be better here
@app.route("/v1/cases")
def cases():
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)

    try:
        if lat is not None:
            lat: int = round(lat)
        if lon is not None:
            lon: int = round(lon)
    except ValueError:
        return Response(None, status=400)

    since = request.args.get("since", type=str)
    if since is not None:
        try:
            since: datetime = dateparser.isoparse(since)
        except ValueError:
            return Response(None, status=400)

    cases = get_cases(lat, lon=lon, since=since)
    return jsonify(cases)
