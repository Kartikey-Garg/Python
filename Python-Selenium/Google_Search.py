from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Set the path to the ChromeDriver executable using the Service class
service = Service("/Users/kartikeygarg/Downloads/chromedriver-mac-arm64/chromedriver")  # Update with the correct path to chromedriver

# Initialize the WebDriver (ChromeDriver in this case)
driver = webdriver.Chrome(service=service)

# Navigate to Google
driver.get("https://www.google.co.in")

# Find the search input field using the updated method
box = driver.find_element(By.XPATH, "//*/form/div[1]/div[1]/div[1]/div/div[2]/input")
print("The input Element is: ", box)

# Enter a query and submit the form
box.send_keys("Send")
box.send_keys(Keys.RETURN)

# Wait for the results page to load
time.sleep(5)

# Close the browser
driver.close()
