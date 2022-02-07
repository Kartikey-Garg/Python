from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https:\\www.google.co.in")
box = driver.find_element_by_xpath("//*/form/div[1]/div[1]/div[1]/div/div[2]/input")
print("The input Element is: ", box)
box.send_keys("Send")
box.send_keys(Keys.RETURN)
time.sleep(5)
driver.close()
