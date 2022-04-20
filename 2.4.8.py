from selenium import webdriver
import math
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    wait = WebDriverWait(browser, 15)
    element = wait.until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "100"))

    browser.find_element(By.XPATH, "//button[@id='book']").click()
    x = calc(browser.find_element(By.XPATH, "//span[@id='input_value']").text)
    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(x)

    browser.find_element(By.XPATH, "//button[@id='solve']").click()

    print(browser.switch_to.alert.text)
