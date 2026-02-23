from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time
import typing

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=chrome_options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.get("https://tinder.com")

def spam_dislike():
    try: 
        dislike_button= WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'gamepad-button') and .//span[text()='Nope']]"))
        )
        dislike_button.click()
    except Exception as e: 
        raise Exception(f"Dislike button failed: {e}")

def retry(func:typing.Callable, retries=7, description= None,attempt=1):
    try:
        func()
        print(f"✓Success on attempt {attempt}: {description or 'Task Completed'}")
    except Exception as e:
        if retries>0:
            print(f"Failed: {e}. Retrying... ({retries} attempts left)")
            retry(func,retries-1,description,attempt+1)
        else: 
            print(f"Failed after all retries: {description or 'Unknown'}")
            raise

try: 
    while(1):
        retry(spam_dislike,description="Spamming dislike button.")
except Exception as e: 
    print(f"Error occured: {e}")