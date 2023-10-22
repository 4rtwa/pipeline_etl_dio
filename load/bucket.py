import requests
def update_user(api_url, user_id ,user_submit):
    response = requests.put(f'{api_url}/users/{user_id}', json=user_submit)
    return True if response.status_code == 200 else False