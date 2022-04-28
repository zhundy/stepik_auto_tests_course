from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By

class Test_Registration(unittest.TestCase):
    # метод который проверяет возможность зарегистрироваться на сайте
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"

        with webdriver.Chrome() as browser:
            browser.get(link)

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

            # с помощью self.assertEqual() проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


    # метод который проверяет возможность зарегистрироваться на сайте
    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"

        with webdriver.Chrome() as browser:
            browser.get(link)

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

            # с помощью self.assertEqual() проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()