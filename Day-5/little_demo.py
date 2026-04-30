# a little demo to show how to use requests library to get data from github api and print the login of the user who created the pull request.
import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_details = response.json()

for i in range(len(complete_details)):
    print(complete_details[i]['user']['login'])
    