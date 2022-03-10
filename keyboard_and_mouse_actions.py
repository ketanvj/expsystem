import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



def setup_function():
    global driver
    driver = webdriver.Chrome(executable_path="../resources/chromedriver.exe")
    #driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://component-showcase.icesoft.org/component-showcase/showcase.iface")
    wait = WebDriverWait(driver, 30)
    table_link = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,'Table')))
    table_link.click()
    row_selection = wait.until\
        (expected_conditions.visibility_of_element_located((By.LINK_TEXT,'Row Selection')))
    row_selection.click()
    select_multiple = wait.until\
        (expected_conditions.visibility_of_element_located((By.XPATH,"//table[@class='iceSelOneRb']/tbody/tr/td[2]/label")))
    select_multiple.click()

def test_row_selection_control_key():
    all_rows = driver.find_elements(By.XPATH, "//table[@class='iceDatTbl']/tbody/tr")
    actions = ActionChains(driver)
    actions.click(all_rows[1])\
            .key_down(Keys.CONTROL)\
            .click(all_rows[3])\
            .click(all_rows[5])\
            .key_up(Keys.CONTROL)\
            .perform()
    # actions.move_to_element().context_click()
    time.sleep(5)


def teardown_function():
    driver.quit()