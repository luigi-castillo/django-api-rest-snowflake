import json

def add_credentials(dict):
    with open('login_credentials.json') as json_file:
        login_credentials = json.load(json_file)
    dict['default'].update(login_credentials)