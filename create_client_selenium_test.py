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


""""
def create_client():
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
    addnewclient = driver.find_element(By.CLASS_NAME, ("add-new"))
    addnewclient.click()

    fullname = driver.find_element(By.ID, ("fullname"))
    phone = driver.find_element(By.ID, ("user_contact"))
    email = driver.find_element(By.ID, ("email"))
    address = driver.find_element(By.ID, ("address"))
    password = driver.find_element(By.ID, ("password"))
    submit = driver.find_element(By.ID, ("submit_new"))

    fullname.send_keys("leo messi")
    phone.send_keys("1010101010")
    email.send_keys("leomessi@gmail.com")
    address.send_keys("argentina")
    password.send_keys("123456789")
    address.send_keys("")

    driver.implicitly_wait(30)
    submit.click()

"""


# def create_customer():
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
clients = driver.find_element(By.LINK_TEXT, ("Customers"))
clients.click()
driver.implicitly_wait(10)
addnewclient = driver.find_element(By.CLASS_NAME, ("add-new"))
addnewclient.click()

fullname = driver.find_element(By.ID, ("fullname"))
phone = driver.find_element(By.ID, ("user_contact"))
email = driver.find_element(By.ID, ("email"))
address = driver.find_element(By.ID, ("address"))
password = driver.find_element(By.ID, ("password"))
driver.implicitly_wait(10)
parent = driver.find_element(By.CLASS_NAME, ("form-control"))
# parent = driver.find_element(By.CLASS_NAME, ("form-control")).find_element(
#   By.TAG_NAME, ("select")).find_element(By.NAME, ("parent"))
#resmax = driver.find_element(By.CLASS_NAME, ("dropdown-item"))
#res = driver.find_element(By.XPATH, ("//*[@id='parent']"))
# driver.find_element(By.XPATH)
driver.implicitly_wait(10)
submit = driver.find_element(By.ID, ("submit_new"))
fullname.send_keys("xavi")
phone.send_keys("9999999999")
email.send_keys("xavi@gmail.com")
address.send_keys("spain")
password.send_keys("123456789")
driver.implicitly_wait(20)
# ActionChains(driver).move_to_element(button).click(button).perform()
driver.implicitly_wait(10)
WebDriverWait(driver, 50).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div[3]/div/form/div[2]/div[8]/select"))).click()
WebDriverWait(driver, 50).until(EC.element_to_be_clickable(
    (By.XPATH, "//html/body/div[3]/div[3]/div[2]/div/div[3]/div/form/div[2]/div[8]/select/option[5]"))).click()

address.send_keys(" ")
# submit.click()
