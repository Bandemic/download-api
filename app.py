from flask import Flask, escape, request, jsonify, Response
import dateutil
import datetime

from db import get_cases

app = Flask(__name__)

app.config["APPLICATION_ROOT"] = "/"


# TODO: instead of a timestamp passing a single UUID might be better here
@app.route("/v1/cases")
def cases():
    try:
        lat: float = round(float(request.args.get("lat")))
        lon: float = round(float(request.args.get("lon")))
    except ValueError:
        return Response(None, status=400)

    try:
        # for updating an existing local list of cases
        since: datetime = dateutil.parser.isoparse(request.args.get("since"))
        cases = get_cases(lat, lon, since)
    except ValueError:
        # for querying the cases for the first time
        cases = get_cases(lat, lon)

    return jsonify(cases)
