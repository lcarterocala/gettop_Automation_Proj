from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page


class SearchResultsPage(Page):

    # locators
    SEARCH_RESULTS = (By.CSS_SELECTOR, 'nav.woocommerce-breadcrumb.breadcrumbs.uppercase')

    def verify_search_results(self, expected_result):
        actual_result = self.driver.find_element(*self.SEARCH_RESULTS).text
        print(f'Search results are: {actual_result[14:]}')
        expected_txt = f'SEARCH RESULTS FOR “{expected_result}”'
        expected_txt = expected_txt.upper()
        print(f'Expected results are: {expected_txt}')
        assert expected_txt == actual_result[14:], f'Error, expected: {expected_result}, got {expected_txt} instead'

    def get_product_name(self):
        product_name = self.driver.find_element(*self.PRODUCT_NAME).text
        print(f'Current product: {product_name}')
        return product_name

    def verify_product_name(self):
        prod_name = self.get_product_name()
        # prod_name = self.driver.find_element(*self.PRODUCT_NAME).text
        actual_name = self.driver.find_element(*self.PRODUCT_NAME).text
        assert actual_name == prod_name, f'Expected {prod_name}'