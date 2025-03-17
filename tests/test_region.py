from pages.main_page import MainPage
from pages.tensor_page import TensorPage
import time
from conftest import driver

def test_second(driver):
    main_page = MainPage(driver)
    tensor_page = TensorPage(driver)

    main_page.open_contacts_page()
    driver.implicitly_wait(3)
    main_page.click_contacts()
    driver.implicitly_wait(3)
    main_page.click_office()
    driver.implicitly_wait(3)
    assert main_page.check_region_and_partners()

    main_page.change_region_to_kamchatka()

    assert main_page.check_kamchatka_region()