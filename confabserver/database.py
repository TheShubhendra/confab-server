"""Database module"""
import os
import psycopg2


DATABASE_URL = os.environ.get("DATABASE_URL")


class ConfabDatabaseConnector:

    def __init__(self):
        self.connection = psycopg2.connect(DATABASE_URL)
        self.cursor = self.connection.cursor()

    def execute(self, sql, values=None):
        self.cursor.execute(sql, values)

    def commit(self):
        self.connection.commit()
