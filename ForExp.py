from selenium import webdriver

dr = webdriver.Chrome()
dr.get("http://suninjuly.github.io/huge_form.html")
elements = dr.find_elements_by_css_selector('[type="text"]')

# цикл
for element in elements:
    element.send_keys("x")

button = dr.find_element_by_css_selector("button.btn")
button.click()

# вывод на экран
alert = dr.switch_to.alert
print(alert.text.split()[-1])
alert.accept()

dr.close()
dr.quit()