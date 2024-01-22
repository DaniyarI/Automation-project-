import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Client_information_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    first_name = "//input[@placeholder='First Name']"
    last_name = "//input[@placeholder='Last Name']"
    address = "//input[@placeholder='Street Address']"
    zip_code = "//input[@placeholder='Zip code']"
    state = "//span[@aria-autocomplete='list']"
    new_york = "//div[text()='New York']"
    telephone = "//input[@placeholder='Phone Number']"
    main_word_3 = "//h1[@class='pt35']"


    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.address)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_state(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.state)))

    def get_new_york(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.new_york)))


    def get_telephone(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.telephone)))

    def get_main_word_3(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word_3)))

    # Actions


    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input First Name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input Last Name")

    def input_address(self, address):
        self.get_address().send_keys(address)
        print("Input Address")

    def input_zip_code(self, zip_code):
        zip_code_element = self.get_zip_code()
        zip_code_element.clear()
        zip_code_element.send_keys(zip_code)
        print("Input Zip Code")

    def click_state(self):
        self.get_state().click()
        print("Click State")

    def click_new_york(self):
        self.get_new_york().click()
        print("Click New York")


    def input_telephone(self, telephone):
        telephone_element = self.get_telephone()
        telephone_element.clear()
        telephone_element.send_keys(telephone)
        print("Input Telephone")



    # Methods

    def input_information(self):
        with allure.step('Input information'):
            Logger.add_start_step(method='input_information')
            self.get_current_url()
            self.input_first_name('John')
            self.input_last_name('Travolta')
            self.input_address('113 S MAIN ST ALBION')
            self.input_zip_code('10006')
            self.click_state()
            self.click_new_york()
            self.input_telephone("212-639-9675")
            self.assert_word(self.get_main_word_3(), 'Checkout')
            Logger.add_end_step(url=self.driver.current_url, method='input_information')





