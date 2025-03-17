from pages.main_page import MainPage
from pages.tensor_page import TensorPage
import time
from conftest import driver

def test_first(driver):

    main_page = MainPage(driver)
    tensor_page = TensorPage(driver)

    main_page.open_contacts_page()
    driver.implicitly_wait(3)
    main_page.click_contacts()
    driver.implicitly_wait(3)
    main_page.click_office()
    driver.implicitly_wait(3)
    main_page.find_and_click_tensor_banner()

    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])

    driver.implicitly_wait(5)
    assert "tensor.ru" in driver.current_url
    assert tensor_page.power_of_people_banner()

    tensor_page.click_about_button()
    driver.implicitly_wait(3)
    assert tensor_page.check_page_url() == True
    driver.implicitly_wait(3)
    assert tensor_page.check_pictures_size() == True

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