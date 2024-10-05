import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

url = "https://practicetestautomation.com/practice-test-login/"

@pytest.fixture
def firefox_driver():
    driver = webdriver.Firefox()
    driver.get(url)
    yield driver
    driver.close()

@pytest.fixture
def chrome_driver():
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver
    driver.close()
