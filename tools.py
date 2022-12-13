import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

def slow_type(page_elem, page_input):
    for letter in page_input:
        time.sleep(float(random.uniform(.02, .1)))
        page_elem.send_keys(letter)


def ad_popup(driver):
    try:
        WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CLASS_NAME, "coupon-poplayer-modal"))) ##coupon popup
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-close"))).click()
    except:
        pass

## Cf https://www.binarydefense.com/mimicking-human-activity-using-selenium-and-python/


def str_to_date(str):
    return datetime.datetime.strptime(str, '%Y-%m-%d %H:%M:%S.%f')



