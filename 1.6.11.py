from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration2.html"
    # link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # inputs = ['Zhundy', 'Bayarov', 'bayarov13@gmail.com', '89244533755', 'Moscow']
    # elements = browser.find_elements(By.TAG_NAME, 'input')
    # [el.send_keys(text) for el, text in zip(elements, inputs)]
    browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("Zhundy")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("Bayarov")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("bayarov13@gmail.com")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']").send_keys("89244533755")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']").send_keys("Moscow")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()