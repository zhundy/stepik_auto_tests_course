from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = calc(browser.find_element(By.XPATH, "//span[@id='input_value']").text)

    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(x)
    browser.find_element(By.XPATH, "//input[@id='robotCheckbox']").click()
    browser.find_element(By.XPATH, "//input[@id='robotsRule']").click()
    browser.find_element(By.XPATH, "//button[@class='btn btn-default']").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()