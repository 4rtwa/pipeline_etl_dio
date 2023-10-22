import pandas as pd
import requests

def read_list(file, header):
    dataframe = pd.read_csv(file)
    user_ids = dataframe[header].tolist()
    return user_ids

def get_user(id, api_url):
    # Utilize sua própria URL se quiser ;)
    # Repositório da API: https://github.com/digitalinnovationone/santander-dev-week-2023-api
    response = requests.get(f"{api_url}/users/{id}")
    return response.json() if response.status_code == 200 else None

def agroup_users(api_url, user_ids):
    users = []
    for id in user_ids:
        user = get_user(id, api_url)
        if user != None:
            users.append(user)
        else:
            continue
    return users