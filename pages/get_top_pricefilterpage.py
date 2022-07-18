from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page


class PriceFilterPage(Page):

    # locators
    HEADER_MENU_IPAD = (By.CSS_SELECTOR, "li[id*='menu-item-470']")
    HEADER_MENU = (By.CSS_SELECTOR, "li[id*='menu-item-4']")
    SLIDER = (By.CSS_SELECTOR, 'span.ui-slider-handle.ui-state-default.ui-corner-all')
    FILTER_BTN = (By.CSS_SELECTOR, 'div.price_slider_wrapper button')
    FILTER_CLOSE = (By.CSS_SELECTOR, '#woocommerce_layered_nav_filters-10 ul li.chosen')
    FILTER_MIN = (By.CSS_SELECTOR, "#woocommerce_layered_nav_filters-10 a[href*='max_price']")
    FILTER_MAX = (By.PARTIAL_LINK_TEXT, 'Max')
    ACTIVE_FILTERS_BAR = (By.LINK_TEXT, 'ACTIVE FILTERS')

    # slider movement
    def slider_move(self):
        actions = ActionChains(self.driver)
        slider_widget = self.driver.find_element(*self.SLIDER)
        actions.click_and_hold(slider_widget)
        actions.move_by_offset(70, 0)
        actions.perform()
        sleep(4)

    def filter_btn_click(self):
        btn = self.driver.wait.until(EC.element_to_be_clickable(self.FILTER_BTN))
        btn.click()
        sleep(4)

    def filter_min_reset(self):
        min_icon = self.driver.find_element(*self.FILTER_MIN)
        min_icon.click()

    def filter_max_reset(self):
        max_icon = self.driver.find_element(*self.FILTER_MAX)
        max_icon.click()

    def verify_filter_reset(self):
        filters_bar = self.driver.wait.until(EC.invisibility_of_element(self.ACTIVE_FILTERS_BAR))
        if bool(filters_bar):
            print('Filters have been reset!')

