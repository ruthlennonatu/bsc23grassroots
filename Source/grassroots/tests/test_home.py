# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Tests(LiveServerTestCase):

    def test_chrome_home_page_title(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome()

        driver.get(self.live_server_url)

        assert "Home" in driver.title

    def test_firefox_home_page_title(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)

        driver.get(self.live_server_url)

        assert "Home" in driver.title

    def test_edge_home_page_title(self):
        options = webdriver.EdgeOptions()
        options.add_argument("--headless")
        driver = webdriver.Edge()

        driver.get(self.live_server_url)

        assert "Home" in driver.title
