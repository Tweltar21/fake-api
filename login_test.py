from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# -----------------------------
# Step 1: Setup Chrome options
# -----------------------------
options = Options()
options.headless = False  # Browser visible

# -----------------------------
# Step 2: Setup Chrome driver
# -----------------------------
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# -----------------------------
# Step 3: Open login page
# -----------------------------
driver.get("file:///C:/Users/Dell/Desktop/fake-api/login.html")
time.sleep(1)

# -----------------------------
# Step 4: Fill username & password
# -----------------------------
driver.find_element(By.ID, "username").send_keys("tweltar")
driver.find_element(By.ID, "password").send_keys("phoongon")

# -----------------------------
# Step 5: Click login button
# -----------------------------
driver.find_element(By.XPATH, "//button[text()='Login']").click()

# -----------------------------
# Step 6: Wait for message div
# -----------------------------
try:
    msg = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "message"))
    ).text
    print("Login result:", msg)
except:
    print("Message div not found or empty")

# -----------------------------
# Step 7: Close browser
# -----------------------------
driver.quit()