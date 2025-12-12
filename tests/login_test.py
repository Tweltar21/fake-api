from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Browser open with auto ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# login.html open
driver.get("file:///C:/Users/Dell/Desktop/fake-api/login.html")

time.sleep(1)

# Fill username and password
driver.find_element(By.ID, "username").send_keys("tweltar")
driver.find_element(By.ID, "password").send_keys("phoongon")

# Click login button
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)

# Close browser
driver.quit()