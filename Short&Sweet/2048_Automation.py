from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('C:\PythonLabs\chromedriver.exe')
browser.get('https://play2048.co/')

grid = browser.find_element_by_tag_name('body')
direction = {0: Keys.UP, 1: Keys.RIGHT, 2: Keys.DOWN, 3: Keys.LEFT}
count = 0
browser.find_element_by_class_name('grid-container').click()
while True:
    count += 1
    grid.send_keys(direction[count % 4])
    try:
        WebDriverWait(browser, .00001).until(EC.presence_of_element_located((By.ID, "game-message game-over")))
        browser.find_element_by_class_name('retry-button').click()
    except:
        print("OK")