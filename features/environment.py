# import allure
# from allure_commons.types import AttachmentType
from app.application import Application

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver
from support.logger import logger, MyListener


# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
bs_user = 'lindsaycarter_we347n'
bs_pw = 'tTiomFaZkZeBYRbYHXWp'
# Allure command:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature


def browser_init(context, test_name):  # this is for use with BrowserStack

# def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(executable_path='\\Users\carte\PycharmProjects\pythonProject2\chromedriver.exe')
    # context.driver = webdriver.Chrome()
    # context.browser = webdriver.Safari()
    # context.driver = webdriver.Safari()
    # context.driver = webdriver.Firefox(executable_path='\\Users\carte\PycharmProjects\pythonProject2\geckodriver.exe')
    # context.browser = webdriver.Firefox()

    # Headless mode
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(chrome_options=options, executable_path='\\Users\\carte\\PycharmProjects\\pythonProject2\\chromedriver.exe')

    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(executable_path=''), MyListener())
    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())

    ### for browerstack ###
    desired_cap = {
         'browser': 'Firefox',
         'os_version': 'Big Sur',
         'os': 'OS X',
         'name': test_name
     }
    url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(20)
    context.driver.wait = WebDriverWait(context.driver, timeout=30)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # logger.info(f'Started scenario: {scenario.name}')
    # browser_init(context)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    # logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')
        # Mark test case as FAILED on BrowserStack:
        context.driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Step failed"}}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
