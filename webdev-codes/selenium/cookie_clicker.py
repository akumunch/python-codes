from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver= webdriver.Chrome(options= chrome_options)