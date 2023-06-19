from hashlib import sha1, sha512
import requests
from pprint import pprint
import base64
from github import Github
import os

message = "Hi Mackenzie"
print (message)

username = "mackenzie1"

#token in env variables
token = os.environ.get('GH_TOKEN')


# url to request
url = f"https://api.github.com/users/{username}"

# make the request and return the json
user_data = requests.get(url).json()

# # # pretty print JSON data
pprint(user_data)


# using an access token
g = Github(login_or_token=token)

# login
g.get_user().login

user = g.get_user()

print(user.name)

#print all the repos
for repo in user.get_repos():
    print(repo)

repoName = "mackenzie1/github-activity-bot"

repo = g.get_repo(repoName)


print(repo.name)

#get readme contents and print
contents2 = repo.get_contents("bot.py")
print(contents2)


contents = repo.get_contents("README.md")
print(contents)

repo.create_file("test2.txt", "test", "test", branch="test")

contents = repo.get_contents("test.txt", ref="test")

print(contents)
