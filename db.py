from flask import Flask
from flask_pymongo import PyMongo  # type: ignore
from datetime import datetime
from typing import Optional, Dict, Any
from uuid import uuid4
from random import randrange, uniform
import time
from itertools import repeat

mongo = PyMongo()


def get_cases(lat: Optional[int], lon: Optional[int], since: Optional[datetime] = None):
    conditions: Dict[str, Any] = {}
    if lat is not None:
        conditions["lat"] = lat
    if lon is not None:
        conditions["lon"] = lon
    if since is not None:
        conditions["since"] = {"$gte": since}
    return (case for case in mongo.db.cases.find(conditions))


def insert_random_cases(n: int):
    for _ in repeat(None, n):
        mongo.db.cases.insert(
            {
                "uuid": uuid4(),
                "trust_level": 1,
                "upload_timestamp": datetime.utcfromtimestamp(
                    randrange(round(time.time()))
                ),
                "lat": round(uniform(-90, 90), 1),
                "lon": round(uniform(-180, 180), 1),
            }
        )
