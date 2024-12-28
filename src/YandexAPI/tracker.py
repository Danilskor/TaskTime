import requests

def get_issues(access_token, org_id):
    url = "https://api.tracker.yandex.net/v2/issues"
    headers = {
        "Authorization": f"OAuth {access_token}",
        "X-Org-ID": org_id
    }

    response = requests.get(url, headers=headers)
    return response.json()

import requests

def create_issue(access_token, org_id, summary, description, queue_key):
    url = "https://api.tracker.yandex.net/v2/issues"
    headers = {
        "Authorization": f"OAuth {access_token}",
        "X-Org-ID": org_id,
        "Content-Type": "application/json"
    }
    data = {
        "summary": summary,
        "description": description,
        "queue": queue_key,
        "type": {
            "id": "TASK"
        }
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

import requests

def update_issue(access_token, org_id, issue_key, summary, description):
    url = f"https://api.tracker.yandex.net/v2/issues/{issue_key}"
    headers = {
        "Authorization": f"OAuth {access_token}",
        "X-Org-ID": org_id,
        "Content-Type": "application/json"
    }
    data = {
        "summary": summary,
        "description": description
    }

    response = requests.patch(url, headers=headers, json=data)
    return response.json()