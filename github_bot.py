import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains


username = "mackenzie.harwood1@gmail.com"
key = "GITHUB_PASSWORD"
password = os.getenv(key, default=None)

repo_url = "https://github.com/mackenzie1/github-activity-bot"

driver = webdriver.Chrome()

driver.get("https://github.com/login")
driver.maximize_window()


inp_username = driver.find_element(By.XPATH, "//input[@id='login_field']")

inp_username.send_keys(username)

inp_password = driver.find_element(By.XPATH, "//input[@id='password']")

inp_password.send_keys(password)

inp_password.send_keys(Keys.ENTER)

time.sleep(2)

repoSearch = "github-activity-bot"

inp_repo_search = driver.find_element(By.XPATH, "//input[@id='dashboard-repos-filter-left']")

inp_repo_search.send_keys(repoSearch)
inp_repo_search.send_keys(Keys.ENTER)

time.sleep(2)

# findRepoByLinktxt =  driver.find_element(By.XPATH, '//a[contains(@href, "github-activity-bot")]')
findRepoByLinktxt =  driver.find_element(By.PARTIAL_LINK_TEXT, '//a[contains(@href, "github-activity-bot")]')

# RepoByLinktxt = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((findRepoByLinktxt)))

time.sleep(2)
# ActionChains(driver).move_to_element(findRepoByLinktxt).click(findRepoByLinktxt).perform()

findRepoByLinktxt.click()

time.sleep(2)

pencilBtn =  driver.find_element(By.XPATH, '//body/div[1]/div[6]/div[1]/main[1]/turbo-frame[1]/div[1]/div[1]/div[1]/div[2]/div[1]/readme-toc[1]/div[1]/div[1]/div[2]/a[1]/*[1]')

pencilBtn.click()

time.sleep(2)

readMeeEditor =  driver.find_element(By.XPATH, '//body/div[1]/div[6]/div[1]/main[1]/turbo-frame[1]/div[1]/react-app[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/main[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/file-attachment[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[5]/div[6]/pre[1]')
readMeeEditor.click()

time.sleep(2)


messageInABot_le = "This edit was made with Selenium!"
#CANT FIND HOW TO LOCATE AND PASS TEXT TO TEXT EDITOR
textbox = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[6]/div[1]/main[1]/turbo-frame[1]/div[1]/react-app[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/main[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/file-attachment[1]/div[1]/div[5]/div[1]/div[1]/div[1]")

time.sleep(2)
textbox.click()
driver.switch_to().active_element(messageInABot_le)

textbox.send_keys(messageInABot_le)

time.sleep(2)

# driver.switch_to().active_element.send_keys(messageInABot_le)
commit = driver.find_element(By.XPATH, "//*[contains(text(), 'Commit changes...')]")

ActionChains(driver).move_to_element(commit).click(commit).perform()
# commit.click


# newaction = ActionChains(driver)
# newaction.move_to_element(buttonnew).send_keys(int(22)).perform()

# selected_contact = driver.find_element("//span[@title='"+contact+"']")
# selected_contact.click()

# textBox = driver.find_element("xpath", "//input[@title='Type a message]")
# textBox2 = "//body/div[@id='app']/div[1]/div[1]/div[5]/div[1]/footer[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]/div[1]/div[1]"

driver.quit()