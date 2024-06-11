

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

"""
Test a negative test scenario with valid email and password
"""
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get('https://accounts.lambdatest.com')

u_name = driver.find_element(By.CSS_SELECTOR, '#email')
u_name.send_keys('ruksana@gmail.com')

u_password = driver.find_element(By.CSS_SELECTOR,'#password')
u_password.send_keys('abcddddddd')


u_login_button = driver.find_element(By.CSS_SELECTOR,'#login-button')
u_login_button.click()



