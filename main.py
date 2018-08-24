import os
import json

from flask import Flask
from flask import request
from github import Github

GITHUB_ACCESS_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN', '')

app = Flask(__name__)
github = Github(GITHUB_ACCESS_TOKEN)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == 'POST':
        payload = json.loads(request.data)
        if payload['action'] == 'opened' or payload['action'] == 'reopened':
            repo = github.get_repo(payload['repository']['id'])
            pr_number = payload['number']
            pr = repo.get_pull(pr_number)
            pr.as_issue().create_comment('This is good')
            pr.merge()
            return ''

    return 'Hello, World!'
