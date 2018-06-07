import requests
import csv

from flask import (
    Blueprint, render_template
)
from flask import current_app, g
from datetime import datetime, timedelta
# from tabulate import tabulate

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('', methods=['GET'])
def users():
    yesterday_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    headers = {
            'App-Token': current_app.app_token,
            'Auth-Token': current_app.auth_token,
        }

    user_list = []
    res = requests.get(url="https://api.hubstaff.com/v1/users", headers=headers)
    if res.status_code == 200:
        users = res.json()['users']
        for user in users:

            project_res = requests.get("https://api.hubstaff.com/v1/users/" +str(user['id']) + "/projects" , headers=headers)
            if project_res.status_code == 200:
                project_list = project_res.json()['projects']

                for project in project_list:

                    time_res = requests.get("https://api.hubstaff.com//v1/custom/by_date/my?start_date="+yesterday_date+"&end_date="+yesterday_date+"&projects=" + str(project['id']) + "users=" + str(user['id']), headers=headers)
                    time_json = time_res.json()
                    if len(time_json['organizations']) > 0:
                        if time_json['organizations'][0]['dates'][0]['users'][0]['projects'][0]['id'] == project['id'] and time_json['organizations'][0]['dates'][0]['users'][0]['id'] == user['id']:
                            project['duration'] = round((time_json['organizations'][0]['dates'][0]['duration']) / 60)

                    if 'duration' in project and project['duration']:
                        project_name = project['name'] + " (" + str(project['duration']) + " minutes)"
                    else:
                        project_name = project['name']
                    user_list.append({
                        user['name']: project_name
                    })

                user['projects'] = project_list

    else:
        users = []



    keys = [user['name'] for user in users]

    print (user_list)
    with open('report.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(user_list)

    return render_template('users.html', users=users)
