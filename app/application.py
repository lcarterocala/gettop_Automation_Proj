from pages.get_tophomepage import HomePage
from pages.get_topheader import Header
from pages.get_topsearch_results_page import SearchResultsPage
from pages.get_topfooter import Footer
from pages.get_top_pricefilterpage import PriceFilterPage
from pages.get_top_cartpage import CartPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.get_tophomepage = HomePage(self.driver)
        self.get_topheader = Header(self.driver)
        self.get_topsearch_results_page = SearchResultsPage(self.driver)
        self.get_topfooter = Footer(self.driver)
        self.get_top_pricefilterpage = PriceFilterPage(self.driver)
        self.get_top_cartpage = CartPage(self.driver)


