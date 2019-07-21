import pytest
from selenium import webdriver
link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="class")  # по умолчанию = function
def dr():
    print("\nstart dr for test..")
    dr = webdriver.Chrome()
    yield dr
    # этот код выполнится после завершения теста
    print("\nquit dr..")
    dr.quit()
    
@pytest.fixture(autouse=True)
def prepare_data():
    print("preparing some critical data for every test")
    
class TestMainPage1(object):
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, dr):
        dr.get(link)
        dr.find_element_by_css_selector("#login_link")
    def test_guest_should_see_basket_link_on_the_main_page(self, dr):
        dr.get(link)
        dr.find_element_by_css_selector(".basket-mini .btn-group > a")
