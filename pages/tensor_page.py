from selenium.webdriver.common.by import By
from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait

class TensorPage:

    def __init__(self, driver):
        self.driver = driver

    def power_of_people_banner(self):
        power_banner = self.driver.find_element(By.XPATH, "//p[text()='Сила в людях']")
        return power_banner.is_displayed()

    def click_about_button(self):
        about_button = self.driver.find_element(By.CSS_SELECTOR, '[href="/about"]')
        about_button.click()

    def check_page_url(self):
        return self.driver.current_url == "https://tensor.ru/about"

    def check_pictures_size(self):
        photos = self.driver.find_elements(By.CSS_SELECTOR, ".tensor_ru-About__block4-content .tensor_ru-About__block4-image img")
        first_photo_size = None
        for photo in photos:
            if not first_photo_size:
                first_photo_size = (photo.size['width'], photo.size['height'])
            else:
                current_photo_size = (photo.size['width'], photo.size['height'])
                if current_photo_size != first_photo_size:
                    return False
        return True

