import requests
from pprint import pprint
import base64
from github import Github
# Authentication is defined via github.Auth
# from github import Auth
import os

message = "Hi Mackenzie"
print (message)

username = "mackenzie1"

key = "GITHUB_PASSWORD"
password = os.getenv(key, default=None)

# auth = Auth.Login(username, password)

# url to request
url = f"https://api.github.com/users/{username}"

# make the request and return the json
user_data = requests.get(url).json()

# pretty print JSON data
pprint(user_data)

# g = Github(auth=auth)

g = Github( )

# login
g.get_user().login

user = g.get_user()

#print all the repos
for repo in user.get_repos():
    print(repo)

#search for name/github-activity-bot
repo = g.search_repositories("{username}/github-activity-bot")[0]

# confirmedRepo = g.get_repo(repo)

#get readme contents and print
contents = repo.get_contents("README.md")
print(contents)

#update read me with some text
# repo.update_file(contents.path, "github activity bot", "bot activity..", contents.sha, branch="main")

# # create a file and commit n push
repo.create_file("test.txt", "commit message", "content of the file")


# contents = repo.get_contents("test.txt", ref="test")
# repo.update_file(contents.path, "more tests", "more tests", contents.sha, branch="test")

# def main():
# 	args = get_args()
# 	g = Github(args.name,args.password)
# 	opt = args.option
# 	if (opt == "branch"):
# 		brancher(args.query, g)
# 	elif (opt == "star"):
# 		starrer(args.query, g)
# 	else:
# 		print("Possible options (-o): 'branch' or 'star'.")