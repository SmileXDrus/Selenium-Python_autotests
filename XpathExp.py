import time
from selenium.webdriver.common.by import By
from selenium import webdriver
link="http://suninjuly.github.io/find_xpath_form"
dr = webdriver.Chrome()
dr.get(link)
# заполнение формы
input1 = dr.find_element_by_tag_name("input").send_keys("Ivan")
input2 = dr.find_element_by_name("last_name").send_keys("Petrov")
input3 = dr.find_element_by_class_name("city").send_keys("Smolensk")
input4 = dr.find_element_by_id("country").send_keys("Russia")
button = dr.find_element_by_css_selector("button.btn").click()

# клик по кнопке
linkf = dr.find_element(By.XPATH, "//button[text()='Отправить']").click()

