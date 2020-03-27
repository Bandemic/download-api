from flask import Flask
from flask_pymongo import PyMongo  # type: ignore
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, Iterator
from uuid import uuid4, UUID
from random import randrange, uniform
import time
from itertools import repeat

mongo = PyMongo()


def get_cases(
    uuid: UUID, lat: Optional[int] = None, lon: Optional[int] = None
) -> Iterator:
    # TODO: prevent timing attacks that could reveal if a UUID is present or not
    conditions: Dict[str, Any] = {}
    if lat is not None:
        conditions["lat"] = lat
    if lon is not None:
        conditions["lon"] = lon
    last_case = mongo.db.cases.find_one({"uuid": uuid})
    if last_case is None:
        conditions["upload_timestamp"] = {"$gte": random_time_in_the_past()}
    else:
        conditions["upload_timestamp"] = {"$gte": last_case["upload_timestamp"]}
    return (case for case in mongo.db.cases.find(conditions))


def random_time_in_the_past() -> datetime:
    # FIXME: use a cryptographically secure RNG
    now = datetime.now()
    one_day_ago = now - timedelta(days=1)
    noise_minutes = randrange(start=0, stop=60 * 24 * 6, step=1)
    # anything between 1 and 7 days ago
    return one_day_ago - timedelta(minutes=noise_minutes)


def insert_random_cases(n: int) -> None:
    for _ in repeat(None, n):
        mongo.db.cases.insert(
            {
                "uuid": uuid4(),
                "trust_level": 1,
                "upload_timestamp": random_time_in_the_past(),
                "lat": round(uniform(-90, 90), 1),
                "lon": round(uniform(-180, 180), 1),
            }
        )
