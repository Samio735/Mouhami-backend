from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Initialize the WebDriver
driver = webdriver.Edge()  # Or specify the path to other WebDriver executables

# Open the main page
driver.get("https://mouhami.vercel.app/joindre")

# Wait for the "Un avocat" button to be clickable
time.sleep(3)

# Optionally, you can perform further actions


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

confirmer_input = driver.find_element(By.CSS_SELECTOR, "[aria-label='Location']")
confirmer_input.send_keys("biskra")


confirmer_input = driver.find_element(By.CLASS_NAME, "z-0")
confirmer_input.click()

time.sleep(5) 
driver.quit()
