import random
import string

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import TestData


""" This class is the parent of all pages"""
"""It contains the generic methods and utilities for all the pages"""


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TestData.Base_URl)
        self.driver.maximize_window()

    def select_drop_down(self, by_locator, value):
        element = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(by_locator))
        self.select = Select(element)
        self.select.select_by_value(str(value))
        ## addding sleep in case if we just need to see what is happening- but not mandatory that it can be removed as well
        time.sleep(2)

    def wait_for_element(self, by_locator):
        element = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator))
        return element

    def do_click(self, by_locator):
        self.wait_for_element(by_locator).click()

    def do_send_keys(self, by_locator, text):
        self.wait_for_element(by_locator).send_keys(text)

    def get_element_text(self, by_locator):
        element = self.wait_for_element(by_locator)
        return element.text

    def is_enabled(self, by_locator):
        element = self.wait_for_element(by_locator)
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 40).until(EC.title_is(title))
        return self.driver.title

    def mouse_hover(self, by_locator):
        element =self.wait_for_element(by_locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_text(self, by_locator):
        element = self.wait_for_element(by_locator)
        return element.text

    def get_random_email_for_create(self):
        randomtext = ''.join(random.choice(string.ascii_letters) for x in range(10))
        return randomtext + "@gmail.com"

    def get_random_day(self):
        return random.randint(1, 30)

    def get_random_month(self):
        return random.randint(1, 13)

    def get_random_year(self):
        return random.randint(1900, 2021)

    def get_random_names(self):
            randomtext = ''.join(random.choice(string.ascii_letters) for x in range(10))
            return randomtext