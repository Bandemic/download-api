from flask import Flask
from flask_pymongo import PyMongo  # type: ignore
from datetime import datetime
from typing import Optional

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://172.31.16.148:27017/bluto"
mongo = PyMongo(app)


def get_cases(lat: Optional[int], lon: Optional[int], since: Optional[datetime] = None):
    conditions = {}
    if lat is not None:
        conditions["lat"] = lat
    if lon is not None:
        conditions["lon"] = lon
    if since is not None:
        conditions["since"] = {"$gte": since}
    return [case for case in mongo.db.cases.find(conditions)]
