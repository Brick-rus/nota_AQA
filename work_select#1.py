from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Открыть страницу https://suninjuly.github.io/selects1.html
url = "http://suninjuly.github.io/selects1.html"
url_2 = "https://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(url_2)

num_1 = int(browser.find_element(By.CSS_SELECTOR, "[id = 'num1']").text)
num_2 = int(browser.find_element(By.CSS_SELECTOR, "[id = 'num2']").text)

# Посчитать сумму заданных чисел
summ = num_1 + num_2
# Выбрать в выпадающем списке значение равное расчитанной сумме
select = Select(browser.find_element(By.CSS_SELECTOR, "[id = 'dropdown']"))
select.select_by_value(str(summ))
# Нажать кнопку "Submit"
button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
button.click()
time.sleep(2)
