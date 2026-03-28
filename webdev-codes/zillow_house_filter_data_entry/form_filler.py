from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FormFiller():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
    def fill_form(self, gform_link, links:list, prices:list, addresses:list):
        for link,price,address in zip(links,prices,addresses):
            self.driver.get(gform_link)
            time.sleep(2)
            inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[jsname='YPqjbf']")
            inputs[0].send_keys(address)
            inputs[1].send_keys(price)
            inputs[2].send_keys(link)
            submit= self.driver.find_element(By.CSS_SELECTOR,".NPEfkd.RveJvd.snByac")
            submit.click()
            time.sleep(3)