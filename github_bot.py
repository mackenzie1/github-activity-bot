import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time


username = "mackenzie.harwood1@gmail.com"
key = "GITHUB_PASSWORD"
password = os.getenv(key, default=None)


driver = webdriver.Chrome()

driver.get("https://github.com/login")
driver.maximize_window()


inp_username = driver.find_element(By.XPATH, "//input[@id='login_field']")

inp_username.send_keys(username)

inp_password = driver.find_element(By.XPATH, "//input[@id='password']")

inp_password.send_keys(password)

inp_password.send_keys(Keys.ENTER)


repoSearch = "github-activity-bot"

inp_repo_search = driver.find_element(By.XPATH, "//input[@id='dashboard-repos-filter-left']")


inp_repo_search.send_keys(repoSearch)
inp_repo_search.send_keys(Keys.ENTER)


findRepoByLinktxt =  driver.find_element(By.XPATH, '//a[contains(@href, "github-activity-bot")]')

findRepoByLinktxt.click()


pencilBtn =  driver.find_element(By.XPATH, '//body/div[1]/div[6]/div[1]/main[1]/turbo-frame[1]/div[1]/div[1]/div[1]/div[2]/div[1]/readme-toc[1]/div[1]/div[1]/div[2]/a[1]/*[1]')

pencilBtn.click()



readMeeEditor =  driver.find_element(By.XPATH, '//body/div[1]/div[6]/div[1]/main[1]/turbo-frame[1]/div[1]/react-app[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/main[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/file-attachment[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[5]/div[6]/pre[1]')
readMeeEditor.click()

messageInABot_le = "This edit was made with Selenium!"
#CANT FIND HOW TO LOCATE AND PASS TEXT TO TEXT EDITOR
driver.find_element(By.CLASS_NAME, "Box-sc-g0xbh4-0 ccyNBX react-code-view-edit").SendKeys(messageInABot_le)

# commit =  driver.find_element(By.XPATH, '//span[contains(text(),'Commit changes...')]')
# commit.click
# selected_contact = driver.find_element("//span[@title='"+contact+"']")
# selected_contact.click()

# textBox = driver.find_element("xpath", "//input[@title='Type a message]")
# textBox2 = "//body/div[@id='app']/div[1]/div[1]/div[5]/div[1]/footer[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]/div[1]/div[1]"

driver.quit()