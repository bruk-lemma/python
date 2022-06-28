from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver


def login():
    driver = webdriver.Chrome(
        '/home/bruk/Downloads/Compressed/chromedriver_linux64_1/chromedriver')
    driver.get("http://3.82.160.140/vms/")
    elem = driver.find_element(By.ID, ("login-email"))
    elem2 = driver.find_element(By.ID, ("login-password"))
    button = driver.find_element(By.CLASS_NAME, ("btn"))
    elem.clear()
    elem.send_keys("2511111111")
    elem2.send_keys("123456")
    button.click()
    driver.get("http://3.82.160.140/vms/superadmin/dashboard")


def nav():
    driver = webdriver.Chrome(
        '/home/bruk/Downloads/Compressed/chromedriver_linux64_1/chromedriver')
    driver.get("http://3.82.160.140/vms/superadmin/dashboard")
    avatar = driver.find_element(By.CLASS_NAME("nav-link"))
    avatar.click()


login()

""""
def client():
    driver = webdriver.Chrome(
        '/home/bruk/Downloads/Compressed/chromedriver_linux64_1/chromedriver')
    driver.get("http://3.82.160.140/vms/superadmin/dashboard")
    avatar = driver.find_element(By.PARTIAL_LINK_TEXT(
        "http://3.82.160.140/vms/superadmin/clients"))
    avatar.click()


login()
"""
