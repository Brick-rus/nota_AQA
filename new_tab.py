# Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти.
# Это делается с помощью команды switch_to.window:
# browser.switch_to.window(window_name)
# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles,
# который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
# new_window = browser.window_handles[1]
# Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
# first_window = browser.window_handles[0]

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()

# Открыть страницу http://suninjuly.github.io/redirect_accept.html
browser.get(url)
# Нажать на кнопку
browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
# Переключиться на новую вкладку

browser.switch_to.window(browser.window_handles[1])
# Пройти капчу для робота и получить число-ответ
x = int(browser.find_element(By.CSS_SELECTOR, "[id='input_value']").text)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


form_input = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
form_input.send_keys(calc(x))
browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
time.sleep(5)