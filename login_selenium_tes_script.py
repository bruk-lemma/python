import email
from multiprocessing.connection import wait
from matplotlib import use
from psutil import users
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(email, password):
    driver = webdriver.Chrome(
        '/home/bruk/Downloads/Compressed/chromedriver_linux64_1/chromedriver')
    driver.get("http://3.82.160.140/vms/")
    elem = driver.find_element(By.ID, ("login-email"))
    elem2 = driver.find_element(By.ID, ("login-password"))
    button = driver.find_element(By.CLASS_NAME, ("btn"))
    elem.clear()
    elem.send_keys(email)
    elem2.send_keys(password)
    # button.click()
    for e in driver.get_log('browser'):
        print(e)
    button.click()


login("2511111111", "123456")
