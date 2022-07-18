from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# init driver
s = Service('C:\\Users\\carte\\Automation\\python-selenium-automation\\chromedriver.exe')
# driver = webdriver.Chrome(executable_path='C:\Users\carte\Automation\python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.wait = WebDriverWait(driver, timeout=10)


# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Watches')

# wait for 500ms (.5 sec)
driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))

# click search
driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'watches' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Testing successful!')

driver.quit()
