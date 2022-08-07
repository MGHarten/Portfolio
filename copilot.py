from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
# to suppress the error messages/logs
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(
    options=options, executable_path=r"C:\WebDrivers\chromedriver.exe"
)

config = {
    'EMAIL': '',
    'PASSWORD': ''
}

web_url = "https://www.github.com"

driver.get(web_url)
assert 'GitHub' in driver.title
if driver.find_element(By.LINK_TEXT, "Sign in"):
    driver.find_element(By.LINK_TEXT, "Sign in").click()
time.sleep(2)
driver.find_element(By.NAME, "login").sendKeys(
    "MGHarten" + Keys.ENTER)
time.sleep(secs=2)
driver.find_element(
    By.ID, "password").send_keys("?C8ttBe5!bsQnPP@" + Keys.ENTER)

time.sleep(2)

data = {}

summary = driver.find_element_by_xpath(
    '//*[@id="account_summary"]/ul/li[1]/span').text
data['Accounty Summary'] = summary

print(data)

driver.close()
