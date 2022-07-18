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
SEARCH_INPUT = (By.CSS_SELECTOR, '#woocommerce-product-search-field-0')
SEARCH_ICON = (By.CSS_SELECTOR, 'a.is-small i.icon-search')
SEARCH_BTN = (By.CSS_SELECTOR, 'div.flex-col button.submit-button')


# open gettop page
driver.get('https://gettop.us/')

# search icon hover
actions = ActionChains(driver)
search_icn = driver.find_element(*SEARCH_ICON)
actions.move_to_element(search_icn)
actions.perform()
sleep(5)


# input text into the search bar
def search_get_top():
    search_inpt = driver.find_element(*SEARCH_INPUT)
    search_inpt.clear()
    search_inpt.send_keys('ipad')


search_get_top()
# click the search button
search_btn = driver.find_element(*SEARCH_BTN)
search_btn.click()





print('Test Successful')
driver.quit()