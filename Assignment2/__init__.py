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
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element(By.XPATH,"//a[text()='Shop']").click()
items_elements = driver.find_elements(By.XPATH, "//h4")
item_list = []
for element in items_elements:
    item_list.append(element.text)

print(item_list)