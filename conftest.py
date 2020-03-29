from flask import Flask
import pytest  # type: ignore

from app import create_app


@pytest.fixture
def app() -> Flask:
    app = create_app()
    return app
