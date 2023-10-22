import json
from os import getenv, environ
import extract.tapper as tp
import transform.strainer as st
import load.bucket as bt

print(environ)
#APP PRINCIPAL

sdw2023_api_url = getenv('OPEN_AI_KEY')

def get_file_and_header(file='SDW2023.csv', header='UserID'):
    file, header = input().split(' ')
    return file, header

user_ids, header = get_file_and_header()

users_list = json.dumps(tp.agroup_users(sdw2023_api_url, tp.read_list(user_ids, header)), indent=2)
iterable_users_list = json.loads(users_list)

for user in iterable_users_list:
    user['news'].append({
        'icon' : 'https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg',
        'description' : f'{st.generate_news(user)}'
    })
    success = bt.update_user(sdw2023_api_url, user['id'], user)

    print(f"user {user['name']} updated? status: {success}")
    print(user['news'])

