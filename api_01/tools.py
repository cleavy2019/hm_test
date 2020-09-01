from selenium import webdriver
from api_01.common import url
import time
def web():

    s = webdriver.Chrome()
    return s

def login(username = "13572862604",password = "862604"):
    time.sleep(3)
    r = web()
    r.get(url)
    r.find_element_by_name("username").send_keys(username)
    r.find_element_by_name("password").send_keys(password)
    time.sleep(5)
    r.find_element_by_id("loginSubmit").click()
    time.sleep(5)

if __name__ == '__main__':
    login()