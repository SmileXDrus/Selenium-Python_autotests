import time
from selenium import webdriver

#Подключение
link = "http://suninjuly.github.io/selects1.html"
dr = webdriver.Chrome()
dr.get(link)

#2 метода создания сообщения
dr.execute_script("alert('Message!');")
time.sleep(3)
dr.execute_script("document.title='Script executing';alert('Message two!');")
time.sleep(3)

#Выход
dr.close()
dr.quit()