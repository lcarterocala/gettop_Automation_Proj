from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Product is selected')
def product_select(context):
    context.app.get_top_cartpage.product_select()


@when('Plus and minus used to manipulate cart item quantity')
def modify_cart_signs(context):
    context.app.get_top_cartpage.modify_cart_signs()


@when('Cart number of items are manually entered')
def cart_input_amount(context):
    context.app.get_top_cartpage.cart_input_amount()


@when('Add to cart button is clicked')
def add_to_cart_btn(context):
    context.app.get_top_cartpage.add_to_cart_btn()


@then('Use arrows to browse through other products')
def arrow_over_btns(context):
    context.app.get_top_cartpage.arrow_over_btns()


@then('Verify product stock status')
def verify_product_status(context):
    context.app.get_top_cartpage.verify_product_status()

