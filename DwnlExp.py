import os 
import time
from selenium import webdriver

#Подключение
dr = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
dr.get(link)

#Элементы
nameF_el = dr.find_element_by_name("firstname")
nameL_el = dr.find_element_by_name("lastname")
email_el = dr.find_element_by_name("email")
file_el = dr.find_element_by_id("file") 
button_el = dr.find_element_by_tag_name("button")

#Получение пути
current_dir = os.path.abspath(os.path.dirname(__file__))    
# получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'DwnlExp1.txt')           


#Заполнение
nameF_el.send_keys("Vlad")
nameL_el.send_keys("Muhin")
email_el.send_keys("element")
#file_el.click()
# добавляем к этому пути имя файла 
file_el.send_keys(file_path)
button_el.click()
time.sleep(2)

#Нажатие на модальное окно
alert = dr.switch_to.alert
alert.accept()
time.sleep(2)

dr.close()
dr.quit()

