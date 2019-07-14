import time
from selenium import webdriver

#Подключение
dr = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
dr.implicitly_wait(4)
dr.get("http://suninjuly.github.io/wait1.html")

#Нажатие на кнопку
button = dr.find_element_by_id("check")
button.click()
message = dr.find_element_by_id("check_message")

#Проверка
if dr.find_element_by_id("check_message").text == "Проверка прошла успешно!":
    print("Верно!")
    dr.close()
    dr.quit()
else:
    print("Ошибка!")
    dr.close()
    dr.quit()