from flask import url_for
from uuid import uuid4, UUID


def test_index_returns_stream_for_existing_uuid(client):
    # TODO: make sure this passed UUID is always recent and exists
    res = client.get(
        url_for("v0.cases.index", uuid=UUID("37ef60df-2183-428d-b651-4c3f3cd94ebb"))
    )
    assert res.status_code == 200
    assert res.is_streamed


def test_index_returns_stream_for_random_uuid(client):
    res = client.get(url_for("v0.cases.index", uuid=uuid4()))
    assert res.status_code == 200
    assert res.is_streamed


def test_index_fails_without_args(client):
    res = client.get(url_for("v0.cases.index"))
    assert res.status_code == 400
    assert res.data == b"Please pass a uuid"
