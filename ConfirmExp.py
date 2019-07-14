import time
import math
from selenium import webdriver

#Подключение
dr = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
dr.get(link)

#Нажатие на кнопку
button_el = dr.find_element_by_tag_name("button")
button_el.click()
time.sleep(1)

#Нажатие на модальное окно
confirm = dr.switch_to.alert
confirm.accept()
time.sleep(1)

# заполнение формы
x_el = dr.find_element_by_id("input_value")
x = x_el.text

#Подсчет
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)

#Заполнение ответа
option = dr.find_element_by_id("answer").send_keys(y)

# клик по кнопке
button = dr.find_element_by_css_selector("button.btn")
button.click()
time.sleep(3)

#Нажатие на модальное окно с Поздравлением
alert = dr.switch_to.alert
alert.accept()
time.sleep(1)

#Выход
dr.close()
dr.quit()