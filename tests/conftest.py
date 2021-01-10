import pytest
from confabserver.database import ConfabDatabaseConnector
from confabserver.server import app


@pytest.fixture
def client():
    """A test client for the app."""
    return app.test_client()


def database_setup():
    connector = ConfabDatabaseConnector()
    with open('../confabserver/schema.sql', 'r') as f:
        schema = f.read()
    connector.execute(schema)
    connector.commit(schema)
