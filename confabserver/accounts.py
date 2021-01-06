"""Module to handle databse operations"""
from .database import ConfabDatabaseConnector
import datetime
def register_user(username:str,password:str,client_data:str):
   connector = ConfabDatabaseConnector()
   sql = """INSERT INTO login_data (username, password, last_login, client_data)VALUES (%s, %s, %s, %s)"""
   print(sql)
   last_login = datetime.datetime.now()
   values = (username,
             password,
             last_login,
             client_data,
             )
   connector.execute(sql, values)
   connector.commit()