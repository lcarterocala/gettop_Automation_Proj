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

# locators
FOOTER_PRODUCTS = (By.CSS_SELECTOR, '.product_list_widget li')
FOOTER_PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_list_widget a')
# FOOTER_PRODUCTS = (By.CSS_SELECTOR, '#footer li')
# PRODUCT_TITLE = (By.CSS_SELECTOR, 'span.product-title')
# PRODUCT_TITLE = (By.CSS_SELECTOR, 'li a span.product-title')
PRODUCT_TITLE = (By.CSS_SELECTOR, 'li .product-title')
PRODUCT_PRICE = (By.CSS_SELECTOR, 'li span.woocommerce-Price-amount.amount')
PRODUCT_CATEGORY_LINKS = (By.CSS_SELECTOR, 'div.menu-main-container li')
FOOTER_CATEGORIES = (By.CSS_SELECTOR, 'span.widget-title')


# open gettop page
driver.get('https://gettop.us/')

# locate & enumerate footer products
footer_prods = driver.find_elements(*FOOTER_PRODUCTS)
product_title = driver.find_elements(*PRODUCT_TITLE)
category_links = driver.find_elements(*PRODUCT_CATEGORY_LINKS)
footer_categories = driver.find_elements(*FOOTER_CATEGORIES)
# new_product_price = product_price[1:]

num_of_products = len(footer_prods)
num_of_prod_cat_links = len(category_links)
print(f'number of products are: {num_of_products}')
print(f'number of category links are: {num_of_prod_cat_links}')
print("\n")

category_bank = []
category_list = ['BEST SELLING', 'LATEST', 'TOP RATED']
for category in footer_categories:
    category_bank.append(category.text)
print('Footer Categories: ', category_bank)
assert category_list == category_bank, f'Error: The footer categories are not present.'

# hover over the footer links
actions = ActionChains(driver)
for links in category_links:
    hover = actions.move_to_element(links)
    hover.perform()
    sleep(1)
    # category_link = links.find_element(*PRODUCT_CATEGORY_LINKS)
    # category_link = links.wait.until(EC.element_to_be_clickable(PRODUCT_CATEGORY_LINKS))
    # actions.move_to_element(category_link)
    # actions.perform()


# for product in footer_prods:
#    product_profile = product.text
#    name = product.find_element(*PRODUCT_TITLE)
#    product_name = name.text
#    price = product.find_element(*PRODUCT_PRICE)
#    product_price = price.text
#    print(product_profile)
#    print("Names: ", product_name)
#    print("PRICE: ", product_price)
#    print("\n")



# for name in product_title:
#    product_name = name.text
#    print('NAME: ', product_name)

# for price in new_product_price:
#    the_price = price.text
#    print('PRICES: ', the_price)

print('Test Successful')
driver.quit()
