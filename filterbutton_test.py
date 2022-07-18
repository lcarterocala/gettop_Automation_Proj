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
RANGE_BAR = (By.CSS_SELECTOR, 'div.ui-slider-range')
# FILTER_BTN = (By.CSS_SELECTOR, 'button.button')
FILTER_BTN = (By.CSS_SELECTOR, 'div.price_slider_wrapper button')
FORM = (By.CSS_SELECTOR, 'aside#woocommerce_price_filter-9')

# open gettop product page
driver.get('https://gettop.us/product-category/ipad/')

# driver.find_element(RANGE_BAR)
# driver.wait.until(EC.visibility_of(RANGE_BAR))

btn = driver.wait.until(EC.element_to_be_clickable(FILTER_BTN))
btn.click()
sleep(5)

print('Test Successful')
driver.quit()




