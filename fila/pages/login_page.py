import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Login_page(Base):

    url = 'https://www.fila.com/account'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    user_name = "(//input[@type='email'])[1]"
    password = "(//input[@type='password'])[1]"
    login_button = "(//button[@type='submit'])[1]"
    accept_cookie_button = "//button[@value='accept']"
    main_word = "//div[@class='account-dashboard-greeting']/h1"


    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_accept_cookie_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.accept_cookie_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login Button")

    def handle_cookie_popup(self):
        try:
            accept_cookie_button = self.get_accept_cookie_button()
            accept_cookie_button.click()
            print("Clicked Accept Cookie Button")
        except Exception as e:
            print(f"An error occurred while handling cookie popup: {str(e)}")



    # Methods

    def authorization(self):
        with allure.step('Authorization'):
            Logger.add_start_step(method='authorization')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.handle_cookie_popup()
            self.input_user_name('qazy6349@gmail.com')
            self.input_password('Travolta1')
            self.click_login_button()
            self.assert_word(self.get_main_word(), 'Welcome, John!')
            Logger.add_end_step(url=self.driver.current_url, method='authorization')




