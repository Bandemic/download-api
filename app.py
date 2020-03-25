from flask import Flask, escape, request, jsonify

from db import get_cases

app = Flask(__name__)

app.config["APPLICATION_ROOT"] = "/"
@app.route("/v1/cases")
def cases():
    # latitude
    lat = request.args.get("lat")
    # longitude
    lon = request.args.get("lon")
    # ISO date
    since = request.args.get("since")

    cases = get_cases(lat, lon, since)
    return jsonify(cases)
