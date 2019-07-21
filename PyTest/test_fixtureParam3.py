import pytest
import math
import time
from selenium import webdriver

@pytest.fixture(scope="session")
def dr():
    print("\nstart dr for test..")
    dr = webdriver.Chrome()
    dr.implicitly_wait(2)
    yield dr
    print("\nquit dr..")
    dr.quit()

urls = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

def correct_answer():
    return str(math.log(int(time.time())))

@pytest.mark.parametrize("url", urls)
def test_get_currect(url, dr):
    link = "{}".format(url)
    dr.get(link)
    dr.find_element_by_tag_name("textarea").send_keys(correct_answer())
    dr.find_element_by_css_selector("button.submit-submission").click()
    el_text = dr.find_element_by_css_selector(".smart-hints__hint")
    text = el_text.text
    assert  text == "Correct!", text
    time.sleep(1)
    
    