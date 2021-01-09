import os
import psycopg2

DATABASE_URL = os.environ.get("DATABASE_URL")

connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()


def delete_tested_user(username):
    sql = "DELETE FROM login_data WHERE username = %s"
    cursor.execute(sql, (username,))
    connection.commit()
