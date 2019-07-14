import time
import math
from selenium import webdriver

#соединение
dr = webdriver.Chrome()
dr.get("http://suninjuly.github.io/get_attribute.html")

#radio
radio = dr.find_element_by_css_selector("[value='robots']").click()
time.sleep(2)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

#Формула
attr = dr.find_element_by_css_selector('[valuex]')
attr_value = attr.get_attribute('valuex')

pole = dr.find_element_by_css_selector('#answer').send_keys(calc(attr_value))
time.sleep(2)

#check
check = dr.find_element_by_css_selector("#robotCheckbox").click()
time.sleep(2)

#Далее
nextButtom = dr.find_element_by_css_selector("button.btn")
nextButtom.click()
time.sleep(2)

dr.close()
dr.quit()

#button = browser.find_element(By.ID, "submit_button")