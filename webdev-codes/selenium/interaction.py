from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver= webdriver.Chrome(options= chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com")


# no_req= driver.find_element(By.XPATH,value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# no_req= driver.find_element(By.CSS_SELECTOR, value= "#articlecount li:nth-child(2) a")

# search = WebDriverWait(driver,10).until(
#     EC.element_to_be_clickable((By.NAME, 'search'))
# ) 
# search.send_keys("Python",Keys.ENTER)

first_name= WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.NAME, 'fName'))
)
last_name= WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.NAME, 'lName'))
)
email= WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.NAME, 'email'))
)
button= WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/form/button'))
)


first_name.send_keys("Akshath")
last_name.send_keys("Thoguparthy")
email.send_keys("ahsdun@gmail.com")
button.click()

