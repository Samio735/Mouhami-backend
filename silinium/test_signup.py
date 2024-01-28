from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Initialize the WebDriver
driver = webdriver.Edge()  # Or specify the path to other WebDriver executables

# Open the main page
driver.get("https://mouhami.vercel.app/joindre")

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Nom']")))

# Fill out the form fields
nom_input = driver.find_element(By.CSS_SELECTOR, "[aria-label='Nom']")
nom_input.send_keys("gouhmaz")

prenom_input = driver.find_element(By.CSS_SELECTOR, "[aria-label='Prenom']")
prenom_input.send_keys("dadiz")

email_input = driver.find_element(By.CSS_SELECTOR, "[aria-label='Email']")
email_input.send_keys("dadiz@gmail.com")

numero_input = driver.find_element(By.CSS_SELECTOR, "[aria-label='Numero de telephone']")
numero_input.send_keys("0777007070")

password_input = driver.find_element(By.CSS_SELECTOR, "[aria-label='Mot de passe']")
password_input.send_keys("dad")

confirmer_input = driver.find_element(By.CSS_SELECTOR, "[aria-label='Confirmer le mot de passe']")
confirmer_input.send_keys("dad")

# Find the submit button and click it
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-primary"))  # Adjust the selector based on your HTML
)
submit_button.click()

# Wait for the URL to change after submitting the form
wait = WebDriverWait(driver, 10)
wait.until(EC.url_contains("https://mouhami.vercel.app/avocat/1/rendez-vous"))

# Optionally, you can add further actions or assertions after the form submission

# Quit the WebDriver
driver.quit()
