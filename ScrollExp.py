import time
import math
from selenium import webdriver

#Подключение
dr = webdriver.Chrome()
link = " http://SunInJuly.github.io/execute_script.html"
dr.get(link)

#Формула
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
#Поиск
num_el = dr.find_element_by_id("input_value")
num = num_el.text

#Ввод
input_el = dr.find_element_by_id("answer").send_keys(calc(num))

#Check
check_el = dr.find_element_by_id("robotCheckbox").click()

#Radio
radio_el = dr.find_element_by_id("robotsRule")
dr.execute_script("return arguments[0].scrollIntoView(true);", radio_el) #спуститься до кнопки
radio_el.click()

#кнопка
button = dr.find_element_by_tag_name("button")
dr.execute_script("return arguments[0].scrollIntoView(true);", button) #спуститься до кнопки
button.click()
time.sleep(5)
dr.quit()