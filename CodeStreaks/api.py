import requests

def get_user_submissions(handle):
    url = f"https://codeforces.com/api/user.status?handle={handle}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch user submissions for {handle}: {response.status_code}")
    data = response.json()
    if data['status'] != 'OK':
        raise Exception(f"API returned an error for {handle}: {data['comment']}")
    return data['result']