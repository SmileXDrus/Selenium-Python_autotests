import math
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver

dr = webdriver.Chrome()
dr.get("http://suninjuly.github.io/selects1.html")

#сумма
def calc(x,y):
  return str(int(x)+int(y))
  
#найти цифры
numWeb1 = dr.find_element_by_id("num1")
num1 = numWeb1.text
numWeb2 = dr.find_element_by_id("num2")
num2 = numWeb2.text
sum = calc(num1,num2)


  
#селектор
select = Select(dr.find_element_by_tag_name("select"))
select.select_by_value(sum)

#отправить кнопка
but = dr.find_element_by_css_selector("button.btn").click()
time.sleep(3)
dr.close()
dr.quit()