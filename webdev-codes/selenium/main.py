from selenium import webdriver
from selenium.webdriver.common.by import By 


chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver= webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

#ul class menu

# upcoming_events= driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a')
# time= driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time')
# upcoming_events= driver.find_elements(By.XPATH,value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
# events= [event.text.split('\n') for event in upcoming_events]
# events=events[0]
# dates= events[::2]
# names= events[1::2]

times_elements= driver.find_elements(By.CSS_SELECTOR, value= '.event-widget time')
times= [time.text for time in times_elements]

names_elements= driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
names= [name.text for name in names_elements]

result= {}

for i in range (len(names)):
    result[i]={'time':times[i],'name':names[i]}

print(result)
# print(time.text)

driver.quit()