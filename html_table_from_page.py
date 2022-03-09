from selenium import webdriver
import pandas

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(executable_path="../../../resources/geckodriver.exe", options=options)
print(driver.name)
driver.maximize_window()
# Opening the browser.
driver.get("http://www.cookbook.seleniumacademy.com/Locators.html")
table = pandas.read_html(driver.page_source)[0]
print(table)
table = pandas.read_html(driver.page_source)[1]
print(table)
table = pandas.read_html(driver.page_source)[2]
print(table)
table = pandas.read_html(driver.page_source)[3]
print(table)


