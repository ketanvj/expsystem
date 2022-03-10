import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../../resources/chromedriver.exe")
driver.maximize_window()
driver.get("https://nichethyself.com/tourism/home.html")
print(driver.title)
driver.get("http://www.google.com")
driver.back()
driver.forward()
print(driver.name) # Name of the browser (chrome, firefox, ie etc)
driver.find_element(by=By.NAME, value='q').send_keys("Selenium")

print(driver.current_url)
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
driver.fullscreen_window()
time.sleep(3)
driver.maximize_window()
print(driver.page_source) # usage ?? any use case
driver.refresh()
