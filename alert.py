# alert = browser.switch_to.alert
# alert.accept()
# Чтобы получить текст из alert, используйте свойство text объекта alert:
#
# alert = browser.switch_to.alert
# alert_text = alert.text

# Другой вариант модального окна, который предлагает пользователю выбор согласиться с сообщением или отказаться
# от него, называется confirm. Для переключения на окно confirm используется та же команда, что и в случае с alert:

# confirm = browser.switch_to.alert
# confirm.accept()
# Для confirm-окон можно использовать следующий метод для отказа:
# confirm.dismiss()

# Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста.
# Чтобы ввести текст, используйте метод send_keys():
# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()

# Открыть страницу http://suninjuly.github.io/alert_accept.html
browser.get(url)
# Нажать на кнопку
browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
# Принять confirm
confirm = browser.switch_to.alert
confirm.accept()
# На новой странице решить капчу для роботов, чтобы получить число с ответом
x = int(browser.find_element(By.CSS_SELECTOR, "[id='input_value']").text)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


form_input = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
form_input.send_keys(calc(x))
browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
time.sleep(5)
