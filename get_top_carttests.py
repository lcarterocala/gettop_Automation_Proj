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
driver.wait = WebDriverWait(driver, timeout=5)
driver.implicitly_wait(5)

# locators
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

# open gettop product page
driver.get('https://gettop.us/product/ipad/')


def modify_cart_signs():
    # click on cart plus to add product
    cart_plus_click = driver.find_element(*CART_PLUS)
    cart_plus_click.click()
    sleep(3)
    # click on cart minus to subtract product
    cart_minus_click = driver.find_element(*CART_MINUS)
    cart_minus_click.click()
    sleep(3)


def cart_input_amount():
    item_num = driver.find_element(*CART_INPUT)
    item_num.clear()
    item_num.send_keys('7')
    sleep(3)


def add_to_cart_btn():
    cart_btn = driver.find_element(*CART_ADD_BTN)
    cart_btn.click()
    print('Item added to cart confirmation is visible!')
    sleep(1)
    # remove_from_cart = driver.find_element(*REMOVE_FROM_CART_ICON)
    # remove_from_cart.click()
    sleep(5)


def arrow_right_btn():
    arrow_right = driver.find_element(*ARROW_RIGHT_ICON)
    # arrow_right.click()
    if bool(arrow_right):
        arrow_right.click()


def arrow_left_btn():
    arrow_left = driver.find_element(*ARROW_LEFT_ICON)
    # arrow_left.click()
    if bool(arrow_left):
        arrow_left.click()


def arrow_over_btns():
    arrow_right_btn()
    arrow_left_btn()


def verify_product_status():
    expected_outcome = 'Out of stock'
    menu_watch = driver.find_element(*MENU_ITEM_WATCH)
    menu_watch.click()
    sleep(2)
    watch_black = driver.find_element(*OUT_OF_STOCK_WATCH)
    watch_black.click()
    sleep(3)
    actual_outcome = driver.find_element(*OUT_OF_STOCK_LABEL)
    assert actual_outcome.text == expected_outcome, f'Error: the item is not out of stock.'
    print('Item out of stock, verified.')


# method calls
modify_cart_signs()
cart_input_amount()
add_to_cart_btn()
sleep(2)
arrow_over_btns()
verify_product_status()

print('Test Successful')
driver.quit()
