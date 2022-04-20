from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    picture = browser.find_element(By.XPATH, "//img")
    picture_value = picture.get_attribute("valuex")
    x = calc(picture_value)
    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(x)
    browser.find_element(By.XPATH, "//input[@id='robotCheckbox']").click()
    browser.find_element(By.XPATH, "//input[@id='robotsRule']").click()
    browser.find_element(By.XPATH, "//button[@class='btn btn-default']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()