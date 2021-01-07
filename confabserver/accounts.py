"""Module to handle databse operations."""
from .database import ConfabDatabaseConnector
import datetime


def register_user(username: str, password: str, client_data: str) -> bool:

    """Function to register user

    This function register a user
    to the database after checking
    whether that username is available or not.
    """
    if is_username_registered(username):
        return False
    connector = ConfabDatabaseConnector()
    sql = """
    INSERT INTO login_data
    (username, password, last_login, client_data)
    VALUES (%s, %s, %s, %s)"""
    last_login = datetime.datetime.now()
    values = (username,
              password,
              last_login,
              client_data,
              )
    connector.execute(sql, values)
    connector.commit()
    return True


def is_username_registered(username: str) -> bool:

    """Function to check username.

    This function check whether a username
    is available or not for new registration."""
    connector = ConfabDatabaseConnector()
    sql = """
    SELECT COUNT(*) FROM login_data
    WHERE username = %s"""
    connector.execute(sql, (username,))
    result = connector.cursor.fetchall()
    return result[0][0]
