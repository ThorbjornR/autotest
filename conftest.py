import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    print('\nЗапуск теста')
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    print('\nТест пройден удачно')