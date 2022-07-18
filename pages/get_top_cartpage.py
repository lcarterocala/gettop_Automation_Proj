from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class CartPage(Page):

    # locators
    PRODUCT_TO_SELECT = (By.CSS_SELECTOR, 'div.product-small.col.has-hover.first.post-186')
    CART_PLUS = (By.CSS_SELECTOR, 'input.plus.button.is-form')
    CART_MINUS = (By.CSS_SELECTOR, 'input.minus.button.is-form')
    # CART_INPUT = (By.CSS_SELECTOR, 'input#quantity buttons_added.input-text.qty.text')
    CART_INPUT = (By.NAME, 'quantity')
    CART_ADD_BTN = (By.CSS_SELECTOR, 'button.single_add_to_cart_button')
    ARROW_ICONS = (By.CSS_SELECTOR, 'li.prod-dropdown.has-dropdown')
    ARROW_RIGHT_ICON = (By.CSS_SELECTOR, 'div.hide-for-off-canvas li.prod-dropdown.has-dropdown i.icon-angle-right')
    ARROW_LEFT_ICON = (By.CSS_SELECTOR, 'div.hide-for-off-canvas li.prod-dropdown.has-dropdown i.icon-angle-left')
    REMOVE_FROM_CART_ICON = (By.CSS_SELECTOR, 'a.remove.remove_from_cart_button')
    MENU_ITEM_WATCH = (By.CSS_SELECTOR, "li[id*='menu-item-471']")
    STOCK_STATUS = (By.CSS_SELECTOR, 'div.product-info p.stock.out-of-stock')
    # OUT_OF_STOCK_WATCH = (By.CSS_SELECTOR, "div.out-of-stock-label")
    OUT_OF_STOCK_WATCH = (By.CSS_SELECTOR, "div.product-small.col.has-hover.out-of-stock")
    OUT_OF_STOCK_LABEL = (By.CSS_SELECTOR, 'p.stock.out-of-stock')

    def product_select(self):
        product = self.driver.find_element(*self.PRODUCT_TO_SELECT)
        product.click()

    def modify_cart_signs(self):
        # click on cart plus to add product
        cart_plus_click = self.driver.find_element(*self.CART_PLUS)
        cart_plus_click.click()
        sleep(3)
        # click on cart minus to subtract product
        cart_minus_click = self.driver.find_element(*self.CART_MINUS)
        cart_minus_click.click()
        sleep(3)

    def cart_input_amount(self):
        item_num = self.driver.find_element(*self.CART_INPUT)
        item_num.clear()
        item_num.send_keys('7')
        sleep(3)

    def add_to_cart_btn(self):
        cart_btn = self.driver.find_element(*self.CART_ADD_BTN)
        cart_btn.click()
        print('Item added to cart confirmation is visible!')
        # remove_from_cart = driver.find_element(*REMOVE_FROM_CART_ICON)
        # remove_from_cart.click()
        sleep(5)

    def arrow_right_btn(self):
        arrow_right = self.driver.find_element(*self.ARROW_RIGHT_ICON)
        if bool(arrow_right):
            arrow_right.click()

    def arrow_left_btn(self):
        arrow_left = self.driver.find_element(*self.ARROW_LEFT_ICON)
        if bool(arrow_left):
            arrow_left.click()

    def arrow_over_btns(self):
        self.arrow_right_btn()
        self.arrow_left_btn()

    def verify_product_status(self):
        expected_outcome = 'Out of stock'
        menu_watch = self.driver.find_element(*self.MENU_ITEM_WATCH)
        menu_watch.click()
        sleep(2)
        watch_black = self.driver.find_element(*self.OUT_OF_STOCK_WATCH)
        watch_black.click()
        sleep(3)
        actual_outcome = self.driver.find_element(*self.OUT_OF_STOCK_LABEL)
        assert actual_outcome.text == expected_outcome, f'Error: the item is not out of stock.'
        print('Item out of stock, verified.')