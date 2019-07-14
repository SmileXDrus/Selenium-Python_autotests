import time
import math
from selenium import webdriver

#Подключение
dr = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
dr.get(link)

#Нажатие на кнопку
button_el = dr.find_element_by_css_selector(".btn")
button_el.click()
time.sleep(1)

#Можно найти название вкладки по title
#title_el = dr.find_element_by_css_selector("title")
#title_value = title_el.text

#Переход на другую вкладку (явно указываем, хоть у нас и так по нажатию перейдет на новую вкладку)
new_w = dr.window_handles[1]
dr.switch_to.window(new_w)

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
time.sleep(5)

#Нажатие на модальное окно с Поздравлением
alert = dr.switch_to.alert
alert.accept()

#Выход
dr.close()
dr.quit()