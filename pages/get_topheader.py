from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page


class Header(Page):

    # locators
    SEARCH_INPUT = (By.CSS_SELECTOR, '#woocommerce-product-search-field-0')
    SEARCH_ICON = (By.CSS_SELECTOR, 'a.is-small i.icon-search')
    SEARCH_BTN = (By.CSS_SELECTOR, 'div.flex-col button.submit-button')
    HEADER_MENU_IPAD = (By.CSS_SELECTOR, "li[id*='menu-item-470']")
    HEADER_MENU = (By.CSS_SELECTOR, "li[id*='menu-item-4']")
    SLIDER = (By.CSS_SELECTOR, 'span.ui-slider-handle.ui-state-default.ui-corner-all')
    FILTER_BTN = (By.CSS_SELECTOR, 'div.price_slider_wrapper button')
    FILTER_CLOSE = (By.CSS_SELECTOR, '#woocommerce_layered_nav_filters-10 ul li.chosen')
    FILTER_MIN = (By.CSS_SELECTOR, "#woocommerce_layered_nav_filters-10 a[href*='max_price']")
    FILTER_MAX = (By.PARTIAL_LINK_TEXT, 'Max')

    def search_icon_hover(self):
        actions = ActionChains(self.driver)
        search_icon = self.find_element(*self.SEARCH_ICON)
        actions.move_to_element(search_icon)
        actions.perform()
        sleep(7)

    def search_gettop(self, search_word):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(search_word)

    def search_button_click(self):
        search_btn = self.driver.find_element(*self.SEARCH_BTN)
        # search_btn = self.driver.find_element(*self.SEARCH_BTN)
        # self.click(search_btn)
        search_btn.click()

    def header_menu_select(self, search_word):
        search_word = search_word.upper()
        menu = self.driver.find_elements(*self.HEADER_MENU)
        for item in menu:
            if item.text == search_word:
                item.click()
                break
