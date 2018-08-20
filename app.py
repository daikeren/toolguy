import os
import json

from flask import Flask
from flask import request
from github import Github

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    payload = json.loads(request.data)
    print(payload)
    return 'Hello, World!'
