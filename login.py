from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml
import time

conf = yaml.safe_load(open('loginDetails.yml'))
myFbEmail = conf['fb_user']['email']
myFbPassword = conf['fb_user']['password']

driver = webdriver.Chrome()
FB_login = "//*[@id='email']"
FB_pass = "//*[@id='pass']"
FB_click = "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button"

def login(url,usernameId, username, passwordId, password, submit_buttonId):
    driver.get(url)
    #driver.find_element(By.XPATH, Xpath_login)
    driver.find_element(By.XPATH, FB_login).send_keys(myFbEmail)
    driver.find_element(By.XPATH, FB_pass).send_keys(myFbPassword)
    driver.find_element(By.XPATH, FB_click).click()
#   driver.find_element("id", "pass").send_keys(password)
#   driver.find_element("id", "u_0_5_Tp").click()


   
login("https://www.facebook.com/", FB_login, myFbEmail, FB_pass, myFbPassword, "loginbutton")
time.sleep(10)