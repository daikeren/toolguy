import os
import json
import time

from flask import Flask
from flask import request
from github import Github

GITHUB_ACCESS_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN', '')

app = Flask(__name__)
g = Github(GITHUB_ACCESS_TOKEN)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    payload = json.loads(request.data)

    if payload['action'] == 'open' or payload['action'] == 'reopened':
        full_name = payload['repository']['full_name']
        print(full_name)
        repo = g.get_repo(payload['repository']['id'])
        pr_number = payload['number']
        pr = repo.get_pull(pr_number)
        pr.as_issue().create_comment('This is good')

# TODO: Need to wait for mergeable
        while 1:
            time.sleep(1)
            if pr.mergeable:
                pr.merge()
                return ''

    return 'Hello, World!'
