from selenium import webdriver

driver = webdriver.Chrome()

first_name_field = driver.find_element_by_id("firstname-input")

last_name_field = driver.find_element_by_name("last-name")

submit_button = driver.find_element_by_id("submit-button")