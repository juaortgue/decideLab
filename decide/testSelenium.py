from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/")
print('Title: %s' % driver.title)
driver.quit()
