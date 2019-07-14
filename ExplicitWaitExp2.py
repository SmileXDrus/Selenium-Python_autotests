import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver

#Настройка
opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
#Подключение
dr = webdriver.Chrome(chrome_options=opt)
dr.get("http://suninjuly.github.io/explicit_wait2.html")

butt = dr.find_element_by_id("book")
#Нажатие на кнопку
text = WebDriverWait(dr, 12).until(
        ec. text_to_be_present_in_element((By.ID, "price"), "10000")
    )
butt.click()  

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
button = dr.find_element_by_css_selector("button[id ='solve']")
button.click()
time.sleep(3)

#Нажатие на модальное окно с Поздравлением
alert = dr.switch_to.alert
alert.accept()
time.sleep(1)

#Выход
dr.close()
dr.quit()