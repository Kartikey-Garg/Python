from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome("chromedriver.exe")
driver.get("https://m.facebook.com/login.php")
login=driver.find_element_by_xpath("//*[@id='m_login_email']")
login.send_keys("your_email_id@domain.name")
password=driver.find_element_by_xpath("//*[@id='m_login_password']")
password.send_keys("#_Include_stdlib.h_57_@")
password.send_keys(Keys.RETURN)
time.sleep(5)
driver.close()
