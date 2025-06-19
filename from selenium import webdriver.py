from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
# Launch Chrome automatically with the correct driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open the target website
driver.get("https://rahulshettyacademy.com/client")
# Click on the register link (Assuming it’s visible or already navigated to register page)
# Fill the form fields
firstName = driver.find_element(By.ID, "firstName")
firstName.send_keys("vanshita")
lastName = driver.find_element(By.ID, "lastName")
lastName.send_keys("pandey")
userEmail = driver.find_element(By.ID, "userEmail")
userEmail.send_keys("imvanshita30@gmail.com")
userMobile = driver.find_element(By.ID, "userMobile")
userMobile.send_keys("7898785340")











