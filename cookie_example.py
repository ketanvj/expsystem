
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def setup_module(module):
    global driver
    driver = webdriver.Firefox(executable_path="../resources/geckodriver.exe")
    driver.maximize_window()

def test_firefix():
    driver.get("https://nichethyself.com/tourism/home.html")
    driver.add_cookie({'name': 'username', 'value': 'stc123'})
    driver.add_cookie({'name': 'password', 'value': '12345'})
    driver.add_cookie({'name': 'choice', 'value': 'customized_tours'})
    print("username cookie value is - ", driver.get_cookie('username'))
    print("All cookies  - ", driver.get_cookies())
    driver.delete_cookie('choice')
    print("All cookies  after deleting choice - ", driver.get_cookies())
    driver.delete_all_cookies()
    print("All cookies after deleting all  - ", driver.get_cookies())
    time.sleep(4)
    print(driver.title)

def test_firefix_google():
    driver.get("https://www.google.com")
    driver.find_element(By.NAME, 'q').send_keys("Selenium Training")

def teardown_module(module):
    driver.quit()