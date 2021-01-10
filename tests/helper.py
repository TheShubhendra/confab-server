from confabserver.database import ConfabDatabaseConnector


def delete_tested_user(username):
    connector = ConfabDatabaseConnector()
    """Delete user from database after testing."""
    sql = "DELETE FROM login_data WHERE username = %s"
    connector.execute(sql, (username,))
    connector.commit()
