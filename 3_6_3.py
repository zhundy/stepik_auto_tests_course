import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

# answer = math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])
def test_ufo_messenge(browser, links):
    # Открываем страницу и в поле вводим правильный ответ.
    link = f"{links}"
    browser.get(link)
    time.sleep(5)
    answer = math.log(int(time.time()))
    browser.find_element(By.XPATH, "//textarea").send_keys(str(answer))

    # Отправляем ответ.
    browser.find_element(By.XPATH, "//button[@class='submit-submission']").click()

    # Проверяем ответ.
    time.sleep(5)
    text = browser.find_element(By.XPATH, "//pre[@class='smart-hints__hint']").text

    # Проверка тестов.
    assert text == "Correct!", "Тест не прошел, что-то пошло не то"