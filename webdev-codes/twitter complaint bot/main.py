#promised download speed = 200mbps, assuming 200 mbps upload speed
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time
import typing

PROMISED_DOWN= 400
PROMISED_UP= 400

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

class InternetSpeedTwitterBot():

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.up=0
        self.down=0
    def get_internet_speed(self) -> tuple:

        self.driver.get("https://www.speedtest.net")
        try:
            start_button= WebDriverWait(self.driver,3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label='start speed test - connection type multi']"))
            )
            start_button.click()

            time.sleep(60)

            close_ad= self.driver.find_element(By.ID, "closeIconHit")
            close_ad.click()

            self.down= round(float(self.driver.find_element(By.CSS_SELECTOR, "span[data-download-status-value]").text))

            self.up= round(float(self.driver.find_element(By.CSS_SELECTOR, "span[data-upload-status-value]").text))

        except Exception as e:
            print(f"Error occured: {e}")


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com")
        if (self.down<PROMISED_DOWN and self.up<PROMISED_UP):
            self.message= f"Hey example_ISP, why is my internet speed {self.down}down/{self.up}up when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up"
            try:
                text_field= WebDriverWait(self.driver,5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-offset-key].public-DraftStyleDefault-ltr"))
                )
                text_field.click(   )
                text_field.send_keys(self.message)
                post_button= self.driver.find_element(By.CSS_SELECTOR,"button[data-testid='tweetButtonInline']")
                post_button.click()
            except Exception as e:
                print(f"Error Occured: {e}")
        else:
            print("Speed is fine.")
istb= InternetSpeedTwitterBot()
istb.get_internet_speed() #istb.up , istb.down
print(istb.up, istb.down)
istb.tweet_at_provider()
