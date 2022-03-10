import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def setup_function():
    global driver
 #   driver = webdriver.Chrome(executable_path="../resources/chromedriver.exe")
    driver = webdriver.Firefox(executable_path="../resources/geckodriver.exe")
    driver.maximize_window()
    driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver");
    global wait
    wait = WebDriverWait(driver, 30)

def test_move_to_element():
    menu = driver.find_element(By.ID, "sub-menu")
    #Create the object for Action Chains
    actions = ActionChains(driver)
    actions.move_to_element(menu)
    # perform the operation on the element
    actions.perform()
    time.sleep(3)
    # google = wait.until \
    #     (expected_conditions.visibility_of_element_located((By.ID, 'link2')))
    google = driver.find_element(By.ID, "link2") # Is this better or it is safe to wait??
    actions.move_to_element(google)
    google.click()
    time.sleep(3)


def teardown_function():
    driver.quit()
