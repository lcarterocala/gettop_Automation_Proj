from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page


class Footer(Page):

    # locators
    FOOTER_CATEGORIES = (By.CSS_SELECTOR, 'span.widget-title')
    FOOTER_PRODUCTS = (By.CSS_SELECTOR, '.product_list_widget li')
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'li .product-title')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'li span.woocommerce-Price-amount.amount')
    STAR_RATING = (By.CSS_SELECTOR, '#footer div.star-rating')
    COPY_RIGHT = (By.CSS_SELECTOR, 'div.copyright-footer')
    PRODUCT_CATEGORY_LINKS = (By.CSS_SELECTOR, 'div.menu-main-container li')
    GO_TO_TOP_BTN = (By.CSS_SELECTOR, 'a#top-link')

    def verify_footer_categories(self):
        footer_categories = self.driver.find_elements(*self.FOOTER_CATEGORIES)
        category_bank = []
        category_list = ['BEST SELLING', 'LATEST', 'TOP RATED']
        for category in footer_categories:
            category_bank.append(category.text)
        print('Footer Categories are present: ', category_bank)
        assert category_list == category_bank, f'Error: The footer categories are not present.'

    def verify_footer_products(self):
        footer_products = self.driver.find_elements(*self.FOOTER_PRODUCTS)
        num_of_products = len(footer_products)

        for product in footer_products:
            product_profile = product.text
            name = product.find_element(*self.PRODUCT_TITLE)
            product_name = name.text
            price = product.find_element(*self.PRODUCT_PRICE)
            product_price = price.text
            star_rating = self.driver.find_element(*self.STAR_RATING)
            starred_product = star_rating.text
            assert product_name, 'Error: Product name should not be blank'
            assert product_price, 'Error: Product should have a price'
            assert starred_product, 'This product does not have a star rating yet'
        print('Number of products in footer: ', num_of_products)

    def verify_copyright_present(self):
        copy_right = self.driver.find_element(*self.COPY_RIGHT)
        assert copy_right, 'Copy right is not present in the pages footer'
        print('Copyright is present in the footer')

    def verify_product_category_links(self):
        product_category_links = self.driver.find_elements(*self.PRODUCT_CATEGORY_LINKS)
        num_of_links = len(product_category_links)
        actions = ActionChains(self.driver)
        for links in product_category_links:
            hover = actions.move_to_element(links)
            hover.perform()
            sleep(1)
        print(f'There are {num_of_links} product category links in the footer. ')
        print('Hover feature of links, exploited during this test!')

    def go_to_top_btn(self):
        go_top_btn = self.driver.find_element(*self.GO_TO_TOP_BTN)
        go_top_btn.click()
        sleep(4)

