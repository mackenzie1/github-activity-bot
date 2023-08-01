import requests
from pprint import pprint
from github import Github
import os
from random import randrange

username = "mackenzie1"


token = os.getenv("TOKEN")

password = os.getenv("GH_PASSWORD")
# url to request
url = f"https://api.github.com/users/{username}"

# make the request and return the json
user_data = requests.get(url).json()

# pretty print JSON data
# pprint(user_data)

# using an access token
# g = Github(login_or_token=token)
g = Github(username, password)

# g = Github(username, token)

user = g.get_user()

print(user)

user.login()

message = "Hi " + username + "!"
print (message)

print( "Username: " + username)



#repo search
repoName =  "mackenzie1/github-activity-bot"

repo = g.get_repo(repoName)


print("Found the correct repo: "+repo.name)


randomNumber = str(randrange(100))

repo.create_file("test"+randomNumber+".txt", "test"+ randomNumber , "test"+randomNumber, branch="test")

contents = repo.get_contents("test.txt", ref="test")

print(contents)

confirmationMessage = "Congrats!! Your github activity bot has succuessfully run! Check out the test branch on your github-actvivity-bot repo to confirm changes were made. Thanks for the attention (: <3 "
print(confirmationMessage)
