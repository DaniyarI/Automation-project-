import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Cart_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    checkout_button = "//button[@class='button-fancy-large']"
    main_word_2 = "//th[@class='section-header header-total-price']"




    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_main_word_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word_2)))




    # Actions


    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click Checkout Button")







    # Methods

    def product_confirmation(self):
        with allure.step('Product confirmation'):
            Logger.add_start_step(method='product_confirmation')
            self.get_current_url()
            self.assert_word(self.get_main_word_2(), 'SUBTOTAL')
            self.click_checkout_button()
            Logger.add_end_step(url=self.driver.current_url, method='product_confirmation')










