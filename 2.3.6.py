from selenium import webdriver
import math
from time import sleep
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    browser.find_element(By.XPATH, "//button[@class='trollface btn btn-primary']").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = calc(browser.find_element(By.XPATH, "//span[@id='input_value']").text)
    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(x)

    browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()

    print(browser.switch_to.alert.text)
    sleep(3)
