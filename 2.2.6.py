from selenium import webdriver
import math
from time import sleep
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    x = calc(browser.find_element(By.XPATH, "//span[@id='input_value']").text)
    input_value = browser.find_element(By.XPATH, "//input[@id='answer']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_value)
    input_value.send_keys(x)

    browser.find_element(By.XPATH, "//input[@id='robotCheckbox']").click()
    browser.find_element(By.XPATH, "//input[@id='robotsRule']").click()
    browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
    sleep(7)
