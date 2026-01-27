import time
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chr_op  = Options()
chr_op.add_experimental_option("detach", True)

ser_ob = Service(r"C:\Users\HP\PycharmProjects\Selenium_with_Python\Drivers\chromedriver.exe")
driver = webdriver.Chrome(options=chr_op, service=ser_ob)



driver.get("https://practice.expandtesting.com/dynamic-id")
# driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 20)

try:

    xpath_selector = "//button[contains(@type,'button') and contains(normalize-space(),'Button with Dynamic ID')]"





    btn = wait.until(EC.presence_of_element_located((By.XPATH, xpath_selector)))


    driver.execute_script("arguments[0].scrollIntoView();", btn)


    wait.until(EC.element_to_be_clickable((By.XPATH, xpath_selector)))

    print(f"Button Text: {btn.text}")
    btn.click()
    print("Success: Clicked successfully!")
    print("checking again button status")
    # btn.click()
    print(f"Button Text: {btn.text}")
    btn.click()


except Exception as e:
    print(f"Timeout ya Error: {type(e).__name__}")


time.sleep(2)
driver.quit()