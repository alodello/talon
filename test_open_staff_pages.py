from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
TESTING_URL = "https://electronics.lnu.edu.ua/about/staff/"


@pytest.fixture
def driver() -> webdriver.Chrome:
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(TESTING_URL)
    return chrome_driver


def test_ua_staff_pages(driver: webdriver.Chrome):
    div_container = driver.find_element(By.CLASS_NAME, "language-switcher")
    components = div_container.find_elements(By.CSS_SELECTOR, "*")
    if components:
        components[0].click()

    components = driver.find_elements(By.CLASS_NAME, "name")
    default_page_title = driver.title
    for component in components:
        container = component.find_elements(By.CSS_SELECTOR, "*")
        if not container:
            assert False
        try:
            container[1].click()
            if driver.title == default_page_title:
                assert False
            driver.back()
        except Exception:
            if not container[1].text:
                continue
            assert False
    assert True


def test_eng_staff_pages(driver: webdriver.Chrome):
    components = driver.find_elements(By.CLASS_NAME, "name")
    default_page_title = driver.title
    for component in components:
        container = component.find_elements(By.CSS_SELECTOR, "*")
        if not container:
            assert False
        try:
            container[1].click()
            if driver.title == default_page_title:
                assert False
            driver.back()
        except Exception:
            if not container[1].text:
                continue
            assert False
    assert True