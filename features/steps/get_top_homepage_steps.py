from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

SEARCH_INPUT = (By.CSS_SELECTOR, '#woocommerce-product-search-field-0')
SEARCH_RESULTS = (By.CSS_SELECTOR, 'nav.woocommerce-breadcrumb.breadcrumbs.uppercase')


@given('Open home page')
def open_homepage(context):
    # context.driver.get('https://gettop.us/')
    context.app.get_tophomepage.open_homepage()


@when('Mouse hover on search icon')
def search_icon_hover(context):
    context.app.get_topheader.search_icon_hover()


@when('Search for {search_word}')
def search_gettop(context, search_word):
    # context.driver.find_element(*SEARCH_INPUT).send_keys(search_word)
    # context.driver.find_element(*SEARCH_BTN).click()
    context.app.get_topheader.search_gettop(search_word)


@when('{search_word} is selected from menu bar')
def header_menu_select(context, search_word):
    context.app.get_topheader.header_menu_select(search_word)

# @when('Search for {search_word}')
# def search_gettop(context, search_word):
    # context.driver.find_element(*SEARCH_INPUT).send_keys(search_word)
    # context.driver.find_element(*SEARCH_BTN).click()
    # context.app.gettop_header.search_gettop(search_word)


@then('Click on search icon')
def search_button_click(context):
    context.app.get_topheader.search_button_click()


@then('Verify search results for {expected_result}')
def verify_search_results(context, expected_result):
    # actual_result = context.driver.find_element(*SEARCH_RESULTS).text
    # print(f'Search results are: {actual_result[14:]}')
    # expected_txt = f'SEARCH RESULTS FOR “{expected_result}”'
    # expected_txt = expected_txt.upper()
    # print(f'Expected results are: {expected_txt}')
    # assert expected_txt == actual_result[14:], f'Error, expected: {expected_result}, got {expected_txt} instead'
    context.app.get_topsearch_results_page.verify_search_results(expected_result)


@then('Verify footer shows Best Selling, Latest, Top Rated categories')
def verify_footer_categories(context):
    context.app.get_topfooter.verify_footer_categories()


@then('Verify products in footer have price, name, star-rating')
def verify_footer_products(context):
    context.app.get_topfooter.verify_footer_products()


@then('Verify copyright is present in the footer')
def verify_copyright_present(context):
    context.app.get_topfooter.verify_copyright_present()


@then('Verify product category links in footer are working')
def verify_product_category_links(context):
    context.app.get_topfooter.verify_product_category_links()


@then('Verify presence and function of go back to top button')
def go_to_top_btn(context):
    context.app.get_topfooter.go_to_top_btn()
