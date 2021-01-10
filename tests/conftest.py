import pytest
from confabserver.database import ConfabDatabaseConnector
from confabserver.server import app
import datetime

@pytest.fixture
def client():
    """A test client for the app."""
    return app.test_client()


@pytest.fixture(scope="session", autouse=True)
def database_setup(request):
    connector = ConfabDatabaseConnector()
    sql = """CREATE TABLE IF NOT EXISTS login_data(
user_id SERIAL PRIMARY KEY,
username varchar(100) NOT NULL,
password varchar (100) NOT NULL,
token varchar (100),
last_login TIMESTAMP,
client_data varchar(100));"""
    connector.execute(sql)
    connector.commit()


@pytest.fixture(scope="session", autouse=True)
def setup_tables(request):
    connector = ConfabDatabaseConnector()
    sql = """
    INSERT INTO login_data
    (username, password, last_login, client_data)
    VALUES (%s, %s, %s, %s)"""
    last_login = datetime.datetime.now()
    values = ("unavailable-username-availibilty-test",
              "unit-test",
              last_login,
              "unit-test",
              )
    connector.execute(sql, values)
    connector.commit()
    sql = """
    INSERT INTO login_data
    (username, password, last_login, client_data)
    VALUES (%s, %s, %s, %s)"""
    last_login = datetime.datetime.now()
    values = ("olduser-register-test",
              "unit-test",
              last_login,
              "unit-test",
              )
    connector.execute(sql, values)
    connector.commit()