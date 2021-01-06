"""Main server file to handle HTTP API requests """
import os
import pyscopg2
from flask import Flask, request


TOKEN = os.environ.get("TOKEN")
DATABASE_URL = os.environ.get("DATA")
app = Flask(__name__)


@app.route('/api/login',methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

