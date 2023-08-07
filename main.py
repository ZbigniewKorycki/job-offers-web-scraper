from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get("https://www.pracuj.pl/")

cookie_agreement = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="button-submitCookie"]')))
cookie_agreement.click()


time.sleep(300)
driver.quit()

