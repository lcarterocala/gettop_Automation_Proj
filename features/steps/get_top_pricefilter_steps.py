from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Filter bar is adjusted')
def slider_move(context):
    context.app.get_top_pricefilterpage.slider_move()


@when('Filter button is clicked')
def filter_btn_click(context):
    context.app.get_top_pricefilterpage.filter_btn_click()


@then('Close the applied Min filter')
def filter_min_reset(context):
    context.app.get_top_pricefilterpage.filter_min_reset()


@then('Close the applied Max filter')
def filter_max_reset(context):
    context.app.get_top_pricefilterpage.filter_max_reset()


@then('Verify price filter has been reset')
def verify_filter_reset(context):
    context.app.get_top_pricefilterpage.verify_filter_reset()

