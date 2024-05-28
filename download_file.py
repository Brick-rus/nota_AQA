from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

url = "https://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()


# Открыть страницу http://suninjuly.github.io/file_input.html
browser.get(url)
# Заполнить текстовые поля: имя, фамилия, email
name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
name.send_keys('name')
last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
last_name.send_keys('famaly')
email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
email.send_keys('yandex.ru')
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')
file = browser.find_element(By.CSS_SELECTOR, '[name="file"]')
file.send_keys(file_path)
# Нажать кнопку "Submit"
button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
button.click()
time.sleep(5)