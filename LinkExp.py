import math
import time
from selenium import webdriver
link="http://suninjuly.github.io/find_link_text"
dr = webdriver.Chrome()
dr.get(link)
# зашифрованное имя ссылки
text = str(math.ceil(math.pow(math.pi, math.e)*10000))
linkf = dr.find_element_by_link_text(text)
linkf.click()
time.sleep(1)
# заполнение формы
input1 = dr.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = dr.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = dr.find_element_by_class_name("city")
input3.send_keys("Smolensk")
input4 = dr.find_element_by_id("country")
input4.send_keys("Russia")
button = dr.find_element_by_css_selector("button.btn")
button.click()
