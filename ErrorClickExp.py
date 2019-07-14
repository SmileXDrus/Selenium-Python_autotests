from selenium import webdriver

dr = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
dr.get(link)

button = dr.find_element_by_tag_name("button")
button.click()

assert False, 'NOT PASSED'