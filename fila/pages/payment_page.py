import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Payment_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    continue_to_billing = "//button[@value='Continue']"




    # Getters

    def get_continue_to_billing(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_to_billing)))




    # Actions


    def click_continue_to_billing(self):
        self.get_continue_to_billing().click()
        print("Click Button Finish")






    # Methods

    def payment(self):
        with allure.step('Payment'):
            Logger.add_start_step(method='payment')
            self.get_current_url()
            self.click_continue_to_billing()
            Logger.add_end_step(url=self.driver.current_url, method='payment')









