from flask import Flask
from flask_pymongo import PyMongo  # type: ignore
import dateutil.parser

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://172.31.16.148:27017/bluto"
mongo = PyMongo(app)


def get_cases(lat, lon, since):
    try:
        lat = round(float(lat))
        lon = round(float(lon))
        since = dateutil.parser.isoparse(since)
        return mongo.db.cases.find({lat: lat, lon: lon, since: {"$gte": since}})
    except ValueError:
        return None
