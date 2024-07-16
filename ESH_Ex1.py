from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Set up the WebDriver
driver = webdriver.Chrome()

url = "https://web.eos.bnk-il.com/auth"
driver.get(url)

# define the IDs for user and pass (Taken from looking at the website's elements section)
usernameID = ":r1:"
PasswordID = ":r2:"

# define login button type (Taken from looking at the website's elements section)
Login_ButtonType = "//button[@type='submit']"

# waiting for the page to finish loading
time.sleep(3)

# try and except section to verify username, password and login button are actually exist in the url
try:
    username = driver.find_element(By.ID, usernameID)
    password = driver.find_element(By.ID, PasswordID)
except:
    print("username or password field existence test failure")
    username = "NULL"
    password = "NULL"

try:
    login_button = driver.find_element(By.XPATH, Login_ButtonType)
except:
    print("Login button existence test failure")
    login_button = "NULL"

# sending the login credentials and pressing the login after a validity check of username,password and login button passed
if (username != "NULL") and (password !="NULL") and (login_button!= "NULL"):
    username.send_keys("tzi@allstar.com")
    password.send_keys("297")
    login_button.click()

else:
    print("login failed, one or more parameters required are missing")

#left for debugging can remove once code is complete
time.sleep(2)
# Closing the browser
driver.quit()