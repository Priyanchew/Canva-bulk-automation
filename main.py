from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os
from excel import list_of_names
import pandas as pd
base_url = "https://www.canva.com/design/DAGLmlA3Y1c/AwXul2mheRPy2LO3ipjtVA/edit?utm_content=DAGLmlA3Y1c&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton"

driver_path = r"C:\Program Files\Selenium Drivers\chromedriver-win64"
driver = webdriver.Chrome()
os.environ['PATH'] += driver_path
driver.maximize_window()
driver.get(url=base_url)
driver.implicitly_wait(time_to_wait=15)
try:
    purple_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div/div[1]/div/div[1]/div/div/button'))
    )
    purple_button.click()
except Exception as e:
    print("Cookie consent button not found:", e)
for i in range(len(list_of_names)):
    try:
        if i == 0:
            head = driver.find_element(By.XPATH, '//*[@id=":r0:0"]/div/div/div/main/div[2]/div[1]/div/div/div/div[4]/div/div/div/div[1]/div/div[2]/div[1]/div/div/div/div[18]/div/div/div/p/span')
        else:
            head = driver.find_element(By.XPATH, '//*[@id=":r0:0"]/div/div/div/main/div[2]/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div[18]/div/div/div/p/span')
        driver.execute_script("arguments[0].scrollIntoView(true);", head)
        time.sleep(2)
        head.click()
        head.click()
        time.sleep(2)
        edit = driver.find_element(By.XPATH, "//span[@class='OYPEnA font-feature-liga-off font-feature-clig-off font-feature-calt-off text-decoration-none text-strikethrough-none']")
        edit.send_keys(Keys.CONTROL, 'a')
        edit.send_keys(list_of_names[i])
        dupe = driver.find_element(By.XPATH, "//*[@id=':r0:0']/div/div/div/main/div[2]/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[1]/div[1]/div/div[7]/div/button")
        driver.execute_script("arguments[0].scrollIntoView(true);", dupe)
        dupe.click()
        if i == 0:
            time.sleep(2)
            copy_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id=":r0:0"]/div/div/div/main/div[2]/div[3]/div/div/div/div/div[1]/div[2]/button'))
            )
            copy_button.click()
    except Exception as e:
        print("NOooooooooooooooo", e)
        time.sleep(60)
        break

