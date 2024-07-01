from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = "email"
password = "password"
# Launch the browser
driver = webdriver.Chrome()  # Or webdriver.Firefox() for Firefox
driver.maximize_window()
# Open the website
driver.get("https://www.maxxedcrypto.com/login")

# Find the username input field and enter your email
username_field = driver.find_element(By.ID, "email")
username_field.send_keys(username)

# Find the password input field and enter your password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)

# Find the login button and click on it to submit the form
login_button = driver.find_element(By.XPATH, "//button[text()='Log In']")
login_button.click()

hamburger_button = driver.find_element(By.XPATH, "//button[@class='hamburger animated fadeInLeft is-closed']")
hamburger_button.click()
time.sleep(3)

Manual_faucet = driver.find_element(By.XPATH, "//*[@id='sidebar-wrapper']/ul/div/li[9]/ul/li[1]/a").get_attribute(
    'href')
driver.get(Manual_faucet)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

hamburger_button = driver.find_element(By.XPATH, "//button[@class='hamburger animated fadeInLeft is-closed']")
hamburger_button.click()
time.sleep(3)
dropdown = driver.find_element(By.XPATH, "//*[@id='sidebar-wrapper']/ul/div/li[8]")
dropdown.click()

# Jump to Dice page
option_dice = driver.find_element(By.XPATH, "//a[contains(@href, '/dice')]")
option_dice.click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
