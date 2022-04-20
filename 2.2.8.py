from selenium import webdriver
import math
import os
from time import sleep
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    browser.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Zhundy")
    browser.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Bayarov")
    browser.find_element(By.XPATH, "//input[@name='email']").send_keys("bayarov13@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.XPATH, "//input[@name='file']")
    element.send_keys(file_path)

    browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
    sleep(7)