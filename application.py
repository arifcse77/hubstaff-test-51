import requests

from flask import Flask, render_template
from config import AUTH_TOKEN, APP_TOKEN


app = Flask(__name__)

@app.route('/')
def hello_world():
    headers = {
        'App-Token': APP_TOKEN,
        'Auth-Token': AUTH_TOKEN,
    }
    res = requests.get(url="https://api.hubstaff.com/v1/users", headers=headers)
    if res.status_code == 200:
        users = res.json()['users']
        for user in users:
            project_res = requests.get("https://api.hubstaff.com/v1/users/" +str(user['id']) + "/projects" , headers=headers)
            if project_res.status_code == 200:
                user['projects'] = project_res.json()['projects']
    else:
        users = []
    return render_template('users.html', users=users)