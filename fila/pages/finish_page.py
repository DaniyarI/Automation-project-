import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Finish_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    main_word_4 = "//a[@href='https://www.fila.com/checkout-shipping' and @title='Shipping']"






    # Getters

    def get_main_word_4(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word_4)))






    # Actions






    # Methods

    def finish(self):
        with allure.step('Finish'):
            Logger.add_start_step(method='finish')
            self.get_current_url()
            self.assert_word(self.get_main_word_4(), 'Shipping')
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='finish')









