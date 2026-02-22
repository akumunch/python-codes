from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time
import typing

ACCOUNT_EMAIL = "akshath@test.com"  
ACCOUNT_PASSWORD = "password123"
ADMIN_EMAIL = "admin@test.com"
ADMIN_PASSWORD = "admin123"

classes_booked = 0
waitlists_joined = 0
alr_booked_waitlisted = 0
detailed_list = []


def admin_process():
    pass

def process_class(element, date):
    global classes_booked, waitlists_joined, alr_booked_waitlisted
    
    class_cards = element.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
    for card in class_cards: 
        if "1800" in card.get_attribute("id"):
            class_card = card
    
    button = class_card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
    button_text = button.text
    
    if button_text == 'Booked':
        print(f"✓ Already booked: Spin Class on {date}")
        alr_booked_waitlisted += 1
        status = "Already Booked"
    elif button_text == 'Waitlisted':
        print(f"✓ Already on waitlist: Spin Class on {date}")
        alr_booked_waitlisted += 1
        status = "Already Waitlisted"
    elif button_text == 'Join Waitlist':
        button.click()
        WebDriverWait(driver, 2).until(
            lambda d: button.text == "Waitlisted"
        )
        print(f"✓ Joined waitlist for: Spin Class on {date}")
        waitlists_joined += 1
        status = "New Waitlist"
    else:
        button.click()
        WebDriverWait(driver, 2).until(
            lambda d: button.text == "Booked"
        )
        print(f"✓ Successfully booked: Spin Class on {date}")
        classes_booked += 1
        status = "New Booking"
    
    detailed_list.append((status, date))
    return 1


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

def login():
    email_input = driver.find_element(By.ID, "email-input")
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.ID, "password-input")
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    login2_button = driver.find_element(By.ID, "submit-button")
    login2_button.click()

    try:
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, "schedule-link"))
        )
    except:
        raise Exception("Login failed")

def booking():
    class_schedule = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.ID, "schedule-link"))
    )
    class_schedule.click()

    elements = driver.find_elements(By.CLASS_NAME, "Schedule_dayGroup__y79__")
    for element in elements:
        if "tue" in element.get_attribute("id"):
            tue_element = element
        if "thu" in element.get_attribute("id"):
            thu_element = element
    
    total_tue = process_class(tue_element, tue_element.find_element(By.TAG_NAME, "h2").text)
    total_thu = process_class(thu_element, thu_element.find_element(By.TAG_NAME, "h2").text)

    my_bookings = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.ID, "my-bookings-link"))
    )
    my_bookings.click()

    confimed_bookings = driver.find_elements(By.CSS_SELECTOR, "#confirmed-bookings-section > div")
    waitlist_bookings = driver.find_elements(By.CSS_SELECTOR, "#waitlist-section > div")
    total_found = len(confimed_bookings) + len(waitlist_bookings)
    
    expected_bookings = total_tue + total_thu
    
    print(f'''
--- BOOKING SUMMARY ---
New bookings: {classes_booked}
New waitlist entries: {waitlists_joined}
Already booked/waitlisted: {alr_booked_waitlisted}
Total Tuesday & Thursday 6pm classes: {expected_bookings}

--- DETAILED CLASS LIST ---''')
    status_labels = {
    "New Booking": "🆕 New Booking",
    "New Waitlist": "🆕 New Waitlist",
    "Already Booked": "✓ Already Booked",
    "Already Waitlisted": "✓ Already Waitlisted"
    }   
    for status, date in detailed_list:
        status_label = "[New Booking]" if "Booking" in status else "[New Waitlist]"
        print(f"  • {status_labels[status]} Spin Class on {date}")
    
    print(f"\n--- VERIFICATION RESULT ---")
    print(f"Expected: {expected_bookings} bookings")
    print(f"Found: {total_found} bookings")

    if total_found == expected_bookings:
        print("✅ SUCCESS: All bookings verified!")
    else:
        print("❌ MISMATCH: Bookings don't match!")
        raise Exception(f"Booking mismatch! Expected {expected_bookings}, found {total_found}")
    try: 
        WebDriverWait(driver,2).until(
            EC.presence_of_element_located((By.ID,"empty-bookings-state"))
        )
        raise Exception("Booking Failed")
    except Exception as e:
        if "Booking Failed" in str(e):
            raise

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
    login_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_button.click()
    retry(login, description="Trying to login")
    retry(booking, description="Booking tue1800 and thu 1800 classes")
except Exception as e:  
    print(f"Error: {e}")
