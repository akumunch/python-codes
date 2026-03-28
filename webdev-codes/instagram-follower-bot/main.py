from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

SIMILAR_ACCOUNT = "chefsteps"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

class InstaFollower: 
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def find_followers(self):
        time.sleep(5)
        followers_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"a[href='/{SIMILAR_ACCOUNT}/followers/']"))
        )
        followers_btn.click()
        time.sleep(3)
        self.modal = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//div[contains(@style,'overflow: hidden auto')]"))
        )

    def scroll(self):
        for i in range(10):
            self.driver.execute_script("""
                let modal = document.querySelector("div[role='dialog']");
                let all = modal.querySelectorAll("*");
                for(let el of all){
                    if(el.scrollHeight > el.clientHeight + 10){
                        el.scrollTop += 600;
                    }
                }
            """)
            time.sleep(1.5)

    def follow(self):
        self.scroll()
        all_buttons = self.driver.find_elements(By.XPATH, "//div[text()='Follow']")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "//*[text()='Cancel']")
                cancel_button.click()

if_ = InstaFollower()
if_.find_followers()
while True:
    if_.follow()


