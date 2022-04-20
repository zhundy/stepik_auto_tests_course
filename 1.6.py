from selenium import webdriver
import math
import time

url = 'http://suninjuly.github.io/find_link_text'
try:
    browser = webdriver.Chrome()
    browser.get(url)

    link = browser.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Zhundy")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Bayarov")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Moscow")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(20)
    browser.quit()