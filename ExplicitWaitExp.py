from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver

#Настройка
opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
#Подключение
dr = webdriver.Chrome(chrome_options=opt)
dr.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

button = WebDriverWait(dr, 5).until(
        ec.element_to_be_clickable((By.ID, "check"))
    )
button.click()  

#Проверка
if dr.find_element_by_id("check_message").text == "Проверка прошла успешно!":
    print("Верно!")
    dr.close()
    dr.quit()
else:
    print("Ошибка!")
    dr.close()
    dr.quit()