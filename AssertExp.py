from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
dr = webdriver.Chrome()
dr.get(link)
time.sleep(1)
# Ваш код, который заполняет обязательные поля

input1 = dr.find_element_by_css_selector(".first[placeholder='Введите имя']").send_keys("Vlad")
lastname = dr.find_element_by_css_selector(".second[placeholder='Введите фамилию']").send_keys("Muhin")
email = dr.find_element_by_css_selector(".third[placeholder='Введите Email']").send_keys("muhin@mail.ru")

# Отправляем заполненную форму
button = dr.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = dr.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert  welcome_text == "Поздравляем! Вы успешно зарегистировались!"
dr.close()
dr.quit()
