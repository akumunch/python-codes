from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver= webdriver.Chrome(options= chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

select_english= WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID, 'langSelect-EN'))
)
select_english.click()
accept_cookies= WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.cc_btn.cc_btn_ac3cept_all'))
)
accept_cookies.click()

cookie= WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID, 'bigCookie'))
)

#cursor=product0, grandma=product1, farm=product2, mine=product3, factory=product4, bank=product5

# cursor= WebDriverWait(driver,10).until(
#     EC.element_to_be_clickable((By.ID, 'product0'))
# )
# grandma = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, 'product1'))
# )

# farm = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, 'product2'))
# )

# mine = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, 'product3'))
# )

# factory = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, 'product4'))
# )

# bank = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, 'product5'))
# )

#so when enoguh cookies are there to buy that item the class changes from "product unlocked disabled" to "product unlocked enabled", so after every 5 seconds we have to check what buttons are enabled. how do we do that? should we first write the code inside the loop to find the cursor, grandma, ... etc or we go one by one, product0, product1 and stop the loop when we reach a productx which is disabled? in this loop we can have a variable product which will have the button, when the loop stops, we will have the most expensive item with us. 

total_start_time = time.time()
timeout = time.time() + 5

while (1):
    cookie.click()
    
    #code for what to do after 5s:
    if time.time() > timeout:
        product_number= 0
        
        while True:
            product="product"+str(product_number) #gives the productid

            upgrade_button= driver.find_element(By.ID, product)  #this is the button, i need to access the class of this button
            
            class_upgrade_button= upgrade_button.get_attribute("class") #if class ends with enabled, incremeent product_number, else stop
            
            if class_upgrade_button.endswith("enabled"):
                product_number+=1
            else:
                break
        
        #after the loop breaks, 'upgrade_button' will be the (highest possible upgrade that can be bought(clicked))+1, ie the next product which is diabled
        product_number-=1 #id of product which is highest possible upgrade that can be bought
        if(product_number>=0):  
            product="product"+str(product_number)
            upgrade_button= driver.find_element(By.ID, product)  
            upgrade_button.click()

        timeout = time.time() + 5  # Reset timer
        
        elapsed = time.time() - total_start_time
        print(f"Elapsed time: {elapsed:.1f} seconds")  # Debug
        
        if elapsed >= 300:
        # retry up to 3 times if stale element error occurs
            for attempt in range(3):
                try:
                    cps_value = driver.find_element(By.ID, "cookiesPerSecond").text.split(": ")[1]
                    print(f"Final CPS after 5 minutes: {cps_value}")
                    break
                except:
                    if attempt < 2:  # not the last attempt
                        time.sleep(0.5)  #wait a bit and retry
                    else:
                        print("Could not get CPS, but game completed!")
            break

driver.quit()