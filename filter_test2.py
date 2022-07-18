from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


s = Service('C:\\Users\\carte\\PycharmProjects\\gettop_Automation\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.wait = WebDriverWait(driver, timeout=10)
driver.implicitly_wait(10)

# locators
# FILTER_MAX = (By.CSS_SELECTOR, 'div.widget.woocommerce li.chosen')
# FILTER_MAX = (By.CSS_SELECTOR, "li.chosen a[href*='product-category']")
# FILTER_MAX = (By.CSS_SELECTOR, 'div.category-filtering div.inline-block li.chosen')
# FILTER_MAX = (By.CSS_SELECTOR, 'div.widget_layered_nav_filters li.chosen')
# FILTER_MAX = (By.CSS_SELECTOR, "a[aria-label='Remove filter']")
# FILTER_MAX = (By.CSS_SELECTOR, ".chosen a[rel='nofollow']")
# FILTER_MAX = (By.CSS_SELECTOR, "li.chosen a[href='https://gettop.us/product-category/ipad/']")
# FILTER_MAX = (By.CSS_SELECTOR, "#woocommerce_layered_nav_filters-10 a[href*='min_price']")
FILTER_MAX = (By.PARTIAL_LINK_TEXT, 'Max')

driver.get('https://gettop.us/product-category/ipad/?max_price=800')


def filter_max_reset():
    # fil_max = driver.find_elements(*FILTER_MAX)
    max_icon = driver.find_element(*FILTER_MAX)
    max_icon.click()


filter_max_reset()
sleep(3)

print('Test Successful')
driver.quit()
