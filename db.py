from flask import Flask
from flask_pymongo import PyMongo  # type: ignore
from datetime import datetime
from typing import Optional, Dict, Any

mongo = PyMongo()


def get_cases(lat: Optional[int], lon: Optional[int], since: Optional[datetime] = None):
    conditions: Dict[str, Any] = {}
    if lat is not None:
        conditions["lat"] = lat
    if lon is not None:
        conditions["lon"] = lon
    if since is not None:
        conditions["since"] = {"$gte": since}
    return [case for case in mongo.db.cases.find(conditions)]
