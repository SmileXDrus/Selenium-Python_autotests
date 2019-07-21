import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def dr():
    print("\nstart dr for test..")
    dr = webdriver.Chrome()
    yield dr
    print("\nquit dr..")
    dr.quit()


class TestMainPage1(object):

    def test_guest_should_see_login_link(self, dr):
        dr.get(link)
        dr.find_element_by_css_selector("#login_link")
    
    @pytest.mark.xfail #будет отмечен как XPASS - неожаданно пройденный
    def test_guest_should_see_basket_link_on_the_main_page(self, dr):
        dr.get(link)
        dr.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.xfail #помечен как xfail - проваленный, но ожидаемо
    def test_guest_should_see_search_button_on_the_main_page(self, dr):
        dr.get(link)
        dr.find_element_by_css_selector("button.favorite")