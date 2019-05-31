
from selenium import webdriver
from Clear_Code_Test_Directory import PageElements

driver = webdriver.Chrome()


def enter_first_name(name):
    PageElements.first_name_field.send_keys(name)
    driver.implicitly_wait(120)
    assert PageElements.first_name_field.text


def enter_last_name(last_name):
    PageElements.last_name_field.send_keys(last_name)
    driver.implicitly_wait(120)
    assert PageElements.last_name_field


def submit_data():
    PageElements.submit_button.click()


