from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
TESTING_URL = "https://electronics.lnu.edu.ua/about/staff/"


@pytest.fixture
def driver() -> webdriver.Chrome:
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(TESTING_URL)
    return chrome_driver


def test_ua_mails(driver: webdriver.Chrome):
    div_container = driver.find_element(By.CLASS_NAME, "language-switcher")
    components = div_container.find_elements(By.CSS_SELECTOR, "*")
    if components:
        components[0].click()

    mails = []
    with open("mail.txt", "r") as m_file:
        lines = m_file.readlines()
        for line in lines:
            mails.append(line.replace("\n", ""))

    components = driver.find_elements(By.CLASS_NAME, "email")
    for component in components:
        container = component.find_elements(By.CSS_SELECTOR, "*")
        if not container:
            assert False
        if not container[0].text in mails:
            assert False


def test_eng_mails(driver: webdriver.Chrome):
    components = driver.find_elements(By.CLASS_NAME, "email")
    mails = []
    with open("mail.txt", "r") as m_file:
        lines = m_file.readlines()
        for line in lines:
            mails.append(line.replace("\n", ""))

    for component in components:
        container = component.find_elements(By.CSS_SELECTOR, "*")
        if not container:
            assert False
        if not container[0].text in mails:
            assert False