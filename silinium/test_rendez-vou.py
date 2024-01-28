from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Edge()  # Or specify the path to other WebDriver executables

# Open the main page
driver.get("https://mouhami.vercel.app/avocat/1")

# Find and click the "prendre un rendez vous" button
button = driver.find_element(By.CSS_SELECTOR, "button.bg-primary")
button.click()
print("Button click successful! Redirected to the expected page.")

# Wait until the URL contains the expected substring
wait = WebDriverWait(driver, 10)
wait.until(EC.url_contains("https://mouhami.vercel.app/avocat/1/rendez-vous"))

# Find and click the second button with class "z-0 bg-primary1"
button2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.z-0.bg-primary1")))
button2.click()
print("Button 2 click successful!")

# Adding a brief delay to see the result
time.sleep(5)
# Find the "Annuler" (Cancel) button and click it
try:
    # Find the "Annuler" (Cancel) button and click it
    confirm_button = driver.find_element(By.XPATH, "//button[text()='Confirmer']")
    confirm_button.click()
    print('yes')
except Exception as e:
    print(f"An error occurred: {e}")

time.sleep(5)

# Close the browser
driver.quit()
