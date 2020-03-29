from app import create_app
import pytest  # type: ignore


@pytest.fixture
def app():
    app = create_app()
    return app
