# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait1.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


browser = webdriver.Chrome()
#
url = "https://suninjuly.github.io/explicit_wait2.html"
# Открыть страницу https://suninjuly.github.io/explicit_wait2.html
browser.get(url)
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[id = 'price']"), '100'))

# Нажать на кнопку "Book"
button = browser.find_element(By.CSS_SELECTOR, "[id = 'book']")
button.click()
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
x = int(browser.find_element(By.CSS_SELECTOR, "[id='input_value']").text)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


form_input = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
form_input.send_keys(calc(x))
browser.execute_script("window.scrollBy(0, 100);")
browser.find_element(By.CSS_SELECTOR, "[id='solve']").click()
#button = WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary")))
import pyperclip
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)
