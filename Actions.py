from typing import Type

from selenium import webdriver
from Clear_Code_Test_Directory import TestMethods
from selenium.webdriver.chrome.webdriver import WebDriver

driver = webdriver.Chrome


driver.get("https://cdn.clearcode.pl/2019/05/index2.html?firstname=dscdxs&lastname=dsfds")

try:
    TestMethods.enter_first_name("Oleksii")

    TestMethods.enter_last_name("Leontiev")
    TestMethods.submit_data()
except:
    print("No such elements")


driver.quit()

