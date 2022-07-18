from selenium.webdriver.common.by import By

from pages.base_page import Page


class HomePage(Page):

    # ORDERS_LINK = (By.CSS_SELECTOR, 'a#nav-orders.nav-a.nav-a-2.nav-progressive-attribute')

    def open_homepage(self):
        self.open_page('https://gettop.us/')

