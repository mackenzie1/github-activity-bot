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
# print("Scan QR Code, And then Enter")

# input()
# print("Logged In")

inp_username = driver.find_element(By.XPATH, "//input[@id='login_field']")

inp_username.send_keys(username)
inp_username.send_keys(Keys.ENTER)

inp_password = driver.find_element(By.XPATH, "//input[@id='password']")

inp_password.send_keys(password)
inp_password.send_keys(Keys.ENTER)

time.sleep(2)

submit_btn = driver.find_element(By.XPATH, "//body/div[1]/div[3]/main[1]/div[1]/div[4]/form[1]/div[1]/input[13]")

element = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((submit_btn)))




time.sleep(2)


# selected_contact = driver.find_element("//span[@title='"+contact+"']")
# selected_contact.click()

# textBox = driver.find_element("xpath", "//input[@title='Type a message]")
# textBox2 = "//body/div[@id='app']/div[1]/div[1]/div[5]/div[1]/footer[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]/div[1]/div[1]"

# inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
# input_box = driver.find_element(inp_xpath)
# time.sleep(2)
# textBox.send_keys(text + Keys.ENTER)
# time.sleep(2)

driver.quit()