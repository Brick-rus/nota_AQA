from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

# Считать значение для переменной x.
x = int(browser.find_element(By.CSS_SELECTOR, "[id='input_value']").text)


# Посчитать математическую функцию от x.

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Проскроллить страницу вниз.

browser.execute_script("window.scrollBy(0, 100);")

# Ввести ответ в текстовое поле.
form_input = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
form_input.send_keys(calc(x))

# Выбрать checkbox "I'm the robot".
browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']").click()

# Переключить radiobutton "Robots rule!".
browser.find_element(By.CSS_SELECTOR, '[for = "robotsRule"]').click()
# Нажать на кнопку "Submit".

button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")

button.click()
time.sleep(4)
