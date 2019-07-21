import unittest
import time
from selenium import webdriver

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
rightPhrase = "Поздравляем! Вы успешно зарегистировались!"

def link_t(link):
    dr = webdriver.Chrome()
    dr.get(link)
    
    # Обязательные поля
    input1 = dr.find_element_by_css_selector(".first[placeholder='Введите имя']").send_keys("Vlad")
    lastname = dr.find_element_by_css_selector(".second[placeholder='Введите фамилию']").send_keys("Muhin")
    email = dr.find_element_by_css_selector(".third[placeholder='Введите Email']").send_keys("muhin@mail.ru")
    button = dr.find_element_by_css_selector("button.btn").click()
    
    time.sleep(3)
    return dr.find_element_by_tag_name("h1").text
        


class Tests(unittest.TestCase):
    def test_1(self):       
        self.assertEqual(link_t(link1), "Поздравляем! Вы успешно зарегистировались!", "Сообщение не соответствует")
        
    def test_2(self):
        self.assertEqual(link_t(link2), "Поздравляем! Вы успешно зарегистировались!", "Сообщение не соответствует")

if __name__ == "__main__":
    unittest.main()