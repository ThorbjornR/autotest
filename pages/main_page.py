from selenium.webdriver.common.by import By
from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def open_contacts_page(self):
        self.driver.get("https://saby.ru/")

    def click_contacts(self):
        contacts = self.driver.find_element(By.LINK_TEXT, 'Контакты')
        contacts.click()

    def click_office(self):
        office = self.driver.find_element(By.CSS_SELECTOR, '[href="/contacts"]')
        office.click()

    def find_and_click_tensor_banner(self):
        tensor_banner = self.driver.find_element(By.CSS_SELECTOR, '[href="https://tensor.ru/"]')
        tensor_banner.click()

    def check_region_and_partners(self):
        wait = WebDriverWait(self.driver, 10)
        region_element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Ярославская обл.']")))
        partners_list = self.driver.find_elements(By.CSS_SELECTOR, ".sbisru-Contacts__partner")
        return region_element.is_displayed() and len(partners_list) > 0

    def change_region_to_kamchatka(self):
        wait = WebDriverWait(self.driver, 10)

        region_chooser = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Ярославская обл.']")))
        region_chooser.click()

        kamchatka_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="Камчатский край"]')))
        kamchatka_option.click()

    def check_kamchatka_region(self):
        wait = WebDriverWait(self.driver, 10)
        new_region_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[title="Камчатский край"]')))
        new_partners_list = self.driver.find_elements(By.CSS_SELECTOR, ".sbisru-Contacts__partner")
        return new_region_element.is_displayed() and len(new_partners_list) > 0