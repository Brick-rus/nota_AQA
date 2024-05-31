from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

# На выбор две ссылки


link_bag = "http://suninjuly.github.io/registration2.html"


class TestAbs(unittest.TestCase):
    def test_reg_no_bag(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)  # Тут меняем переменную для прохождения тестов по разным ссылкам
        first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        last_name.send_keys("Ivanov")
        email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        email.send_keys("Ivanov071@yandex.ru")
        phone = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']")
        phone.send_keys("89202202020")
        address = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']")
        address.send_keys("Tula")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        time.sleep(2)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text,
                          "Текст не найден")

    def test_reg_bag(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)  # Тут меняем переменную для прохождения тестов по разным ссылкам
        first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        last_name.send_keys("Ivanov")
        email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        email.send_keys("Ivanov071@yandex.ru")
        phone = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']")
        phone.send_keys("89202202020")
        address = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']")
        address.send_keys("Tula")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        time.sleep(2)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text,
                          "Текст не найден")


if __name__ == "__main__":
    unittest.main()
