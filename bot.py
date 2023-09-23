import requests
from pprint import pprint
from github import Github
import os
from random import randrange

username = "mackenzie1"

#token in env variables
token = os.getenv("GH_TOKEN")

# url to request
url = f"https://api.github.com/users/{username}/api/v3"

# make the request and return the json
# user_data = requests.get(url).json()


# using an access token
# g = Github(login_or_token=token)
g = Github(token)

user = g.get_user("mackenzie1")
print(user)

# g.get_user().login



message = "Hi " + username + "!"
print (message)



#repo search
repoName =  "mackenzie1/github-activity-bot"

repo = g.get_repo(repoName)


print("Found the correct repo: "+repo.name)


randomNumber = str(randrange(100))
# print(randomNumber)

contents = repo.get_contents("text.txt")
print(contents)

createFileMessage = "Creating a new file called test with a random number appended "
print(createFileMessage)

repo.create_file("test"+randomNumber+".txt", "test"+ randomNumber , "test"+randomNumber, branch="test")
# repo.update_file(contents.path, "more tests", "more tests", contents.sha, branch="test")

# contents = repo.get_contents("test.txt", ref="test")

# print(contents)

confirmationMessage = "Congrats!! Your github activity bot has succuessfully run! Check out the test branch on your github-actvivity-bot repo to confirm changes were made."
print(confirmationMessage)
