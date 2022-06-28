from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
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

client = driver.find_element(By.LINK_TEXT(
    "http://3.82.160.140/vms/superadmin/clients"))
client.click()
