from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

usernameFieldElement = driver.find_element(By.ID, "email")
usernameFieldElement.clear()
usernameFieldElement.send_keys("Nellikonelly@mail.ru")

passwordFieldElement = driver.find_element(By.ID, "pass")
passwordFieldElement.clear()
passwordFieldElement.send_keys("Korea2022")

loginButton = driver.find_element(By.NAME, "login")
loginButton.click()

sleep(10)
