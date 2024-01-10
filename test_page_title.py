from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
TESTING_URL = "https://electronics.lnu.edu.ua/about/staff/"


@pytest.fixture
def driver() -> webdriver.Chrome:
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(TESTING_URL)
    return chrome_driver


def test_page_title(driver: webdriver.Chrome):
    eng_title = driver.title
    div_container = driver.find_element(By.CLASS_NAME, "language-switcher")
    components = div_container.find_elements(By.CSS_SELECTOR, "*")
    if components:
        components[0].click()
    ukr_title = driver.title
    assert ukr_title == "Персонал - Факультет електроніки та комп'ютерних технологій" \
           and eng_title == "Staff - Faculty of Electronics and Computer Technologies"