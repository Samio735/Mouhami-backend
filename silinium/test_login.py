from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Edge()  # Or specify the path to other WebDriver executables

# Open the main page
driver.get("https://mouhami.vercel.app/login")
time.sleep(2)
# Find the username field and enter username
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']"))  # Adjust the selector based on your HTML
)
email_input.send_keys("dadiz")
time.sleep(2)
# Find the password field and enter password
password_input = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Mot de passe']"))  # Adjust the selector based on your HTML
)
password_input.send_keys("dad")
time.sleep(2)
# Find the submit button and click it
submit_button = WebDriverWait(driver, 40).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-primary"))  # Adjust the selector based on your HTML
)
submit_button.click()

# Wait for the page to load
# Add more explicit waits if necessary
time.sleep(5)

# Quit the WebDriver
driver.quit()
