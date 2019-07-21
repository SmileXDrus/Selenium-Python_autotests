from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage1():

    @classmethod
    def setup_class(cls):
        print("\nstart dr for test suite..")
        cls.dr = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):
        print("quit dr for test suite..")
        cls.dr.quit()

    def test_guest_should_see_login_link(self):
        self.dr.get(link)
        self.dr.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.dr.get(link)
        self.dr.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("start dr for test..")
        self.dr = webdriver.Chrome()

    def teardown_method(self):
        print("quit dr for test..")
        self.dr.quit()

    def test_guest_should_see_login_link(self):
        self.dr.get(link)
        self.dr.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.dr.get(link)
        self.dr.find_element_by_css_selector(".basket-mini .btn-group > a")
