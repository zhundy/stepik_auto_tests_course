from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc(num1, num2):
    return str(int(num1) + int(num2))

try:
    # link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.XPATH, "//span[@id='num1']").text
    num2 = browser.find_element(By.XPATH, "//span[@id='num2']").text
    sum_num = calc(num1, num2)

    select = Select(browser.find_element(By.XPATH, "//select[@id='dropdown']"))
    select.select_by_value(sum_num)

    browser.find_element(By.XPATH, "//button[@class='btn btn-default']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()