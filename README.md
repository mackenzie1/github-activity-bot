# Github Activity Bot 
## Green out your github activity chart out easily :four_leaf_clover: :chart: :green_heart:

### Set Up
1. Clone this repo

    `git clone https://github.com/mackenzie1/github-activity-bot.git`

2. [Generate a github access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

3. [Add the token to your local enviroment](https://help.knapsack.cloud/article/83-github-personal-access-tokens-local-dev)

4. Install:

   [Install Python](https://www.python.org/downloads/)
      
   [Install PyGithub](https://pygithub.readthedocs.io/en/latest/introduction.html#download-and-install)

5. Change the following variables in [bot.py](bot.py):
   
    Line 7: update with your username


    Line 10: update with the name you used in step 3

6. Create a branch named test in the cloned repo


### Manually Use It!

1. Navigate to the folder where you cloned the repo

2. Open a terminal

3. Run `.\bot.py`

### Github Actions    
*I have set up a workflow for the [bot.py](bot.py) script. It is scheduled on a cron job to run once a day. I am unsure if this will transfer over after cloning. If you would like to set up a github actions for this repo to automate the process even more checkout: [pythonbot.yml](.github/workflows/pythonbot.yml)*


### Video Preview


https://github.com/mackenzie1/github-activity-bot/assets/49001843/9a87979c-113e-4dc6-b556-8182efefed69

### Inspiration
![image](https://github.com/mackenzie1/github-activity-bot/assets/49001843/ed9af5a5-b630-4c77-93b1-f3dc86ee7d59)

Made with: [PyGithub](https://pygithub.readthedocs.io/en/latest/index.html)
