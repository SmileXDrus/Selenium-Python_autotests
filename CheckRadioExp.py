import time
import math

from selenium import webdriver
  
link="http://suninjuly.github.io/math.html"
dr = webdriver.Chrome()
dr.get(link)
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

#checkbox
option1 = dr.find_element_by_css_selector("[for='robotCheckbox']").click()
#radio
option2 = dr.find_element_by_css_selector("[value='robots']").click()
time.sleep(1)

# клик по кнопке
button = dr.find_element_by_css_selector("button.btn")
button.click()

# вывод на экран
alert = dr.switch_to.alert
print(alert.text.split()[-1])
alert.accept()

#Выход
dr.close()
dr.quit()