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
# HEADER_MENU = (By.CSS_SELECTOR, 'ul.header-nav.nav-left')
HEADER_MENU_IPAD = (By.CSS_SELECTOR, "li[id*='menu-item-470']")
HEADER_MENU = (By.CSS_SELECTOR, "li[id*='menu-item-4']")
SLIDER = (By.CSS_SELECTOR, 'span.ui-slider-handle.ui-state-default.ui-corner-all')
FILTER_BTN = (By.CSS_SELECTOR, 'div.price_slider_wrapper button')
FILTER_CLOSE = (By.CSS_SELECTOR, '#woocommerce_layered_nav_filters-10 ul li.chosen')
FILTER_MIN = (By.CSS_SELECTOR, "#woocommerce_layered_nav_filters-10 a[href*='max_price']")
# FILTER_MAX = (By.CSS_SELECTOR, "li.chosen a[href*='product-category']")
# FILTER_MAX = (By.CSS_SELECTOR, 'div.category-filtering div.inline-block li.chosen')
# FILTER_MAX = (By.CSS_SELECTOR, 'div.widget_layered_nav_filters li.chosen')
# FILTER_MAX = (By.CSS_SELECTOR, "a[aria-label='Remove filter']")
# FILTER_MAX = (By.CSS_SELECTOR, ".chosen a[rel='nofollow']")
# FILTER_MAX = (By.CSS_SELECTOR, "li.chosen a[href='https://gettop.us/product-category/ipad/']")
# FILTER_MAX = (By.CSS_SELECTOR, 'div.widget.woocommerce li.chosen')
# FILTER_MAX = (By.CSS_SELECTOR, "#woocommerce_layered_nav_filters-10 a[href*='min_price']")
FILTER_MAX = (By.PARTIAL_LINK_TEXT, 'Max')
ACTIVE_FILTERS_BAR = (By.LINK_TEXT, 'ACTIVE FILTERS')

# open gettop product page
driver.get('https://gettop.us/')


def header_menu(key_word):
    key_word = key_word.upper()
    menu = driver.find_elements(*HEADER_MENU)
    for item in menu:
        if item.text == key_word:
            item.click()
            break


# ipad_link = driver.find_element(*HEADER_MENU_IPAD)
# ipad_link.click()


def slider_move():
    # slider movement
    actions = ActionChains(driver)
    slider_widget = driver.find_element(*SLIDER)
    actions.click_and_hold(slider_widget)
    actions.move_by_offset(70, 0)
    actions.perform()
    sleep(4)


def filter_btn_click():
    btn = driver.wait.until(EC.element_to_be_clickable(FILTER_BTN))
    btn.click()
    sleep(4)


def filter_min_reset():
    min_icon = driver.find_element(*FILTER_MIN)
    min_icon.click()


def filter_max_reset():
    max_icon = driver.find_element(*FILTER_MAX)
    max_icon.click()


def verify_filter_reset():
    filters_bar = driver.wait.until(EC.invisibility_of_element(ACTIVE_FILTERS_BAR))
    if bool(filters_bar):
        print('Filters have been reset!')


# method calls
header_menu('ipad')
slider_move()
filter_btn_click()
filter_min_reset()
filter_max_reset()
sleep(3)
verify_filter_reset()

print('Test Successful')
driver.quit()
