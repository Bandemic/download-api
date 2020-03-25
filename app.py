from flask import Flask, escape, request, jsonify, Response
import dateutil
import datetime

from db import get_cases

app = Flask(__name__)

app.config["APPLICATION_ROOT"] = "/"


# TODO: instead of a timestamp passing a single UUID might be better here
@app.route("/v1/cases")
def cases():
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)
    if lat is None or lon is None:
        return Response(None, status=400)

    try:
        lat: int = round(lat)
        lon: int = round(lon)
    except ValueError:
        return Response(None, status=400)

    since = request.args.get("since")
    if since is None:
        # for querying the cases for the first time
        cases = get_cases(lat, lon)
    else:
        try:
            # for updating an existing local list of cases
            since: datetime = dateutil.parser.isoparse(since)
            cases = get_cases(lat, lon, since)
        except ValueError:
            return Response(None, status=400)

    return jsonify(cases)
