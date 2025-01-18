import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
service_obj1 = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
                      'chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj1)
driver.implicitly_wait(3)
driver.get('https://rahulshettyacademy.com/loginpagePractise/')
driver.find_element(By.XPATH, "//a[@class='blinkingText'][1]").click()
windows_opened1 = driver.window_handles
driver.switch_to.window(windows_opened1[1])
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='inner-box']/h1")))
username = driver.find_element(By.XPATH, "//div[@class='col-md-8']/p/strong/a").text
driver.switch_to.window(windows_opened1[0])
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys("password")
driver.find_element(By.NAME, "signin").click()
time.sleep(2)
print(driver.find_element(By.CSS_SELECTOR,".alert-danger").text)






time.sleep(3)
driver.close()