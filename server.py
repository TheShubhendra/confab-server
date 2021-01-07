"""Main server file to handle HTTP API requests."""
import os
from flask import Flask, request
from confabserver.accounts import (
    register_user,
    is_username_registered,
)

TOKEN = os.environ.get("TOKEN")
DATABASE_URL = os.environ.get("DATA")
app = Flask(__name__)


@app.route('/api/register', methods=["POST"])
def register():
    """Register a user in Confab."""
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    client_data = data["client_data"]
    if register_user(username, password, client_data):
        return "1"
    else:
        return "0"


@app.route('/api/checkusername', methods=["post"])
def checkusername():
    """Check availability of a username."""
    username = request.get_json()["username"]
    if is_username_registered(username):
        return "0"
    else:
        return "1"
