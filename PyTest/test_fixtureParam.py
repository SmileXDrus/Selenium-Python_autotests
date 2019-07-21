import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def dr():
    print("\nstart dr for test..")
    dr = webdriver.Chrome()
    yield dr
    print("\nquit dr..")
    dr.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(dr, language):
    link = "http://selenium1py.pythonanywhere.com/{}/".format(language)
    dr.get(link)
    dr.find_element_by_css_selector("#login_link")
    