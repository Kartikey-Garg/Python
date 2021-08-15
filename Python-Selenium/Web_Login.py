from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome("chromedriver.exe")
driver.get("https://m.facebook.com/login.php")
login=driver.find_element_by_xpath("//*[@id='m_login_email']")
login.send_keys("email")
password=driver.find_element_by_xpath("//*[@id='m_login_password']")
password.send_keys("password")
password.send_keys(Keys.RETURN)
time.sleep(5)
driver.close()
