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


def serach_bar(name):
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
    driver.implicitly_wait(10)
    avatar = driver.find_element(By.CLASS_NAME, ("nav-item"))
    avatar.click()
    users = driver.find_element(By.LINK_TEXT, ("Users"))
    users.click()
    clients = driver.find_element(By.LINK_TEXT, ("Clients"))
    clients.click()
    driver.implicitly_wait(10)
   # addnewclient = driver.find_element(By.CLASS_NAME, ("add-new"))
   # addnewclient.click()

    WebDriverWait(driver, 50).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div[1]/div/div[1]/div[2]/div/label/input"))).send_keys(name)


serach_bar("senay")
serach_bar("joe")
