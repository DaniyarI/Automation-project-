import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    button_men = "(//a[text()='Men'])[1]"
    heritage_apparel = "//a[@class='cat-refinement ' and contains(@href, 'https://www.fila.com/men-heritage')]"
    sweatsuits_tracksuits = "(//a[contains(@href, 'men-heritage-tracksuits')])[5]"
    """Фильтр по Цвету"""
    color = "//dt[text()='Color ']"
    color_black = "//a[@id='swatch-black']"
    color_white = "//a[@id='swatch-white']"
    color_red = "//a[@id='swatch-red']"
    """Фильтр по Размеру"""
    size = "//dt[text()='Size ']"
    size_l = "//a[@id='swatch-L']"
    size_xl = "//a[@id='swatch-XL']"
    """Фильтр по Цене"""
    price = "//dt[contains(text(), 'Price')]"
    fifty = "//a[contains(@href, '50.00') and contains(@href, '100.00') and contains(@title, '$51 - $100')]"
    """Фильтр по Полу"""
    gender = "//dt[contains(text(), 'Gender')]"
    men = "//a[@title='Mens']"
    """Фильтр по Стилю"""
    style = "//dt[contains(text(), 'Apparel Style')]"
    jackets = "//a[@title='Jackets']"
    """Выбор Товара"""
    select_product_1 = "//a[@title='Gonal Zip Jacket']"
    product_1_color = "//a[@title='078 BLEACHED MARL / BLACK']"
    product_1_size = "//a[@title='XL' and @class='swatchanchor' and @role='radio']"
    add_to_bug = "//button[@id='add-to-cart' and @title='Add to Bag' and contains(@class, 'add-to-cart')]"
    view_bag = "//button[@class='checkout']"
    main_word_1 = "//a[text()='Warehouse' and @href='https://www.fila.com/warehouse-sale']"





    # Getters

    def get_button_men(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_men)))

    def get_heritage_apparel(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.heritage_apparel)))

    def get_sweatsuits_tracksuits(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.sweatsuits_tracksuits)))

    def get_color(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.color)))

    def get_color_black(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.color_black)))

    def get_color_white(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.color_white)))

    def get_color_red(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.color_red)))

    def get_size(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.size)))

    def get_size_l(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.size_l)))

    def get_size_xl(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.size_xl)))

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_fifty(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.fifty)))

    def get_gender(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.gender)))

    def get_men(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.men)))

    def get_style(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self. style)))

    def get_jackets(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.jackets)))

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_product_1_color(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_1_color)))

    def get_product_1_size(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_1_size)))

    def get_main_word_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word_1)))

    def get_add_to_bug(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_bug)))

    def get_view_bag(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.view_bag)))



    # Actions


    def click_button_men(self):
        self.get_button_men().click()
        print("Click Button Men")

    def click_heritage_apparel(self):
        self.get_heritage_apparel().click()
        print("Click Button Heritage Apparel")

    def click_sweatsuits_tracksuits(self):
        self.get_sweatsuits_tracksuits().click()
        print("Click Button Sweatsuits Tracksuits")

    def click_color(self):
        self.get_color().click()
        print("Click Button Color")

    def click_color_black(self):
        self.get_color_black().click()
        print("Click Button Color Black")

    def click_color_white(self):
        self.get_color_white().click()
        print("Click Button Color White")

    def click_color_red(self):
        self.get_color_red().click()
        print("Click Button Color Red")

    def click_size(self):
        self.get_size().click()
        print("Click Button Size")

    def click_size_l(self):
        self.get_size_l().click()
        print("Click Button Size L")

    def click_size_xl(self):
        self.get_size_xl().click()
        print("Click Button Size XL")

    def click_price(self):
        self.get_price().click()
        print("Click Button Price")

    def click_fifty(self):
        self.get_fifty().click()
        print("Click Button $50 - $100")

    def click_gender(self):
        self.get_gender().click()
        print("Click Button Gender")

    def click_men(self):
        self.get_men().click()
        print("Click Button Men")

    def click_style(self):
        self.get_style().click()
        print("Click Button Style")

    def click_jackets(self):
        self.get_jackets().click()
        print("Click Button Jackets")

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click Button Select Product 1")

    def click_product_1_color(self):
        self.get_product_1_color().click()
        print("Click Button Product 1 Color")

    def click_product_1_size(self):
        self.get_product_1_size().click()
        print("Click Button Product 1 Size")

    def click_add_to_bug(self):
        self.get_add_to_bug().click()
        print("Click Button Add To Bug")

    def click_view_bag(self):
        self.get_view_bag().click()
        print("Click Button View Bag")







    # Methods

    def select_product(self):
        with allure.step('Select product'):
            Logger.add_start_step(method='select_product')
            self.get_current_url()
            self.click_button_men()
            self.click_heritage_apparel()
            self.click_sweatsuits_tracksuits()
            self.click_color()
            self.click_color_black()
            self.click_color_white()
            self.click_color_red()
            self.click_size()
            self.click_size_l()
            self.click_size_xl()
            self.click_price()
            self.click_fifty()
            self.click_gender()
            self.click_men()
            self.click_style()
            self.click_jackets()
            self.click_select_product_1()
            self.click_product_1_color()
            self.click_product_1_size()
            self.assert_word(self.get_main_word_1(), 'Warehouse')
            self.click_add_to_bug()
            self.click_view_bag()
            Logger.add_end_step(url=self.driver.current_url, method='select_product')







