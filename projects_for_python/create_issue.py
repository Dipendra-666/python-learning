import requests
from requests.auth import HTTPBasicAuth
import json
import os

JIRA_URL = "https://dipendra32.atlassian.net"      

PROJECT_KEY = "DR"
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")

auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def create_task(summary, description=""):
    url = f"{JIRA_URL}/rest/api/3/issue"

    payload = json.dumps({
        "fields": {
            "project": {
                "key": PROJECT_KEY
            },
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": description
                            }
                        ]
                    }
                ]
            },
            "issuetype": {
                "name": "Task"       # Use "Workstream" for workstreams
            }
        }
    })

    response = requests.post(url, data=payload, headers=headers, auth=auth)

    if response.status_code == 201:
        issue = response.json()
        print(f"Created: {issue['key']} — {JIRA_URL}/browse/{issue['key']}")
        return issue
    else:
        print(f"Failed: {response.status_code}")
        print(response.text)
        return None

create_task(
    summary="Set up CI/CD pipeline",
    description="Configure GitHub Actions for automated deployment"
)
tasks = [
    {"summary": "Design database schema", "description": "Create ERD for the new module"},
    {"summary": "Write unit tests", "description": "Cover auth module with tests"},
    {"summary": "Update API docs", "description": "Document new endpoints"},
]

for task in tasks:
    create_task(**task)