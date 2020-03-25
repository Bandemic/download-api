from flask import Flask, escape, request, jsonify, Response
import dateutil

from db import get_cases

app = Flask(__name__)

app.config["APPLICATION_ROOT"] = "/"


# TODO: instead of a timestamp passing a single UUID might be better here
@app.route("/v1/cases")
def cases():
    try:
        lat = round(float(request.args.get("lat")))
        lon = round(float(request.args.get("lon")))
        since = dateutil.parser.isoparse(request.args.get("since"))
    except ValueError:
        return Response(None, status=400)

    cases = get_cases(lat, lon, since)
    return jsonify(cases)
