from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# -----------------------------
# 1️⃣ LambdaTest credentials
# -----------------------------
username = "thwethwemoett"
access_key = "LT_546BrXX0UEe1a9YPXhPwL3N1YxOBlI8jLMwQLigVM1jWeka"

# -----------------------------
# 2️⃣ LambdaTest hub URL
# -----------------------------
url = "https://hub.lambdatest.com/wd/hub"

# -----------------------------
# 3️⃣ Chrome options & capabilities
# -----------------------------
options = Options()
options.set_capability("browserName", "Chrome")
options.set_capability("browserVersion", "latest")

options.set_capability("LT:Options", {
    "username": username,
    "accessKey": access_key,
    "platformName": "Windows 10",
    "project": "FakeAPI Login",
    "build": "Build 1",
    "name": "Login Test"
})

# -----------------------------
# 4️⃣ Start remote browser
# -----------------------------
driver = webdriver.Remote(
    command_executor=url,
    options=options
)

# -----------------------------
# 5️⃣ Open login page (public URL)
# -----------------------------
# Replace this with your public HTML page URL
driver.get("https://yourusername.github.io/fake-api/login.html")

# Wait for page to load
time.sleep(2)

# -----------------------------
# 6️⃣ Fill username & password
# -----------------------------
driver.find_element(By.ID, "username").send_keys("tweltar")    # Fake API username
driver.find_element(By.ID, "password").send_keys("phoongon")  # Fake API password

# -----------------------------
# 7️⃣ Click login button
# -----------------------------
driver.find_element(By.XPATH, "//button[text()='Login']").click()

# -----------------------------
# 8️⃣ Wait for fetch to complete
# -----------------------------
time.sleep(2)

# -----------------------------
# 9️⃣ Read login result from <div id="message">
# -----------------------------
try:
    msg = driver.find_element(By.ID, "message").text
    print("Login result:", msg)
except:
    print("Could not read login result.")

# -----------------------------
# 🔟 Close browser
# -----------------------------
driver.quit()