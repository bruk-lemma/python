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
WebDriverWait(driver, 50).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/nav/div/ul/li[2]"))).click()
addnewclient = driver.find_element(By.CLASS_NAME, ("add-new"))
addnewclient.click()

fullname = driver.find_element(By.ID, ("fullname"))
phone = driver.find_element(By.ID, ("user_contact"))
email = driver.find_element(By.ID, ("email"))
address = driver.find_element(By.ID, ("address"))
password = driver.find_element(By.ID, ("password"))
submit = driver.find_element(By.ID, ("submit_new"))
driver.implicitly_wait(30)

fullname.send_keys("cavani")
phone.send_keys("4578129638")
email.send_keys("cavani@gmail.com")
address.send_keys("gonder")
password.send_keys("123456")
address.send_keys("")
driver.implicitly_wait(30)

# submit.click()
