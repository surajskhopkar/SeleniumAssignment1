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
driver.get('https://rahulshettyacademy.com/angularpractice/shop')

items_list_elements = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
print(items_list_elements)
for element in items_list_elements:
    product_name = element.find_element(By.XPATH, "div/h4/a").text
    if product_name == 'Nokia Edge':
        element.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@value='Purchase']").click()
print(driver.find_element(By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']").text)


time.sleep(5)
driver.close()

