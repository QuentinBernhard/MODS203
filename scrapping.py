from pathlib import Path
import random
import time

from selenium.webdriver.support.wait import WebDriverWait
import tools
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import TabsInteraction

tempsAttente = 3    #temps d'attente en secondes avant qu'il y a un timeout de Webdriverwait.unit()

class Driver:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--disable-blink-features")
        options.add_argument("disable-popup-blocking")
        options.add_argument("disable-notifications")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(ChromeDriverManager().install())



    def connect(self):
        self.driver.get("https://www.doctolib.fr")
        # TabsInteraction.TabsCreation(self.driver, "https://www.doctolib.fr", "")
        # TabsInteraction.switchToTab(self.driver, 0)
        print("Connecting to Doctolib")
        time.sleep(1)


    def getSpecializations(self):

        specializations = []        

        WebDriverWait(self.driver, tempsAttente).until(EC.visibility_of_element_located((By.XPATH, '//input[@class="searchbar-input searchbar-query-input"]')))
        text_area = self.driver.find_element(By.XPATH, '//input[@class="searchbar-input searchbar-query-input"]')

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


        for letter in letters :
            text_area.clear()
            time.sleep(1)
            text_area.send_keys(letter)
            time.sleep(2)

            #getting the first result
            try:
                path = '//button[@class="searchbar-result searchbar-result-active"]'
                WebDriverWait(self.driver, tempsAttente).until(EC.visibility_of_element_located((By.XPATH, path)))
                element = self.driver.find_element(By.XPATH, path)
                specialization = element.get_attribute('id')

                if specialization not in specializations:
                    specializations.append(specialization)
                else:
                    print('Specialization ', specialization, 'already found')
                    
                print(specializations[-1])

                #getting the other results
                try :
                    path = '//button[@class="searchbar-result"]'
                    WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, path)))
                    elements = self.driver.find_elements(By.XPATH, path)
                    
                    for element in elements:
                        specializations.append(element.get_attribute('id'))
                        print(specializations[-1])

                except:
                    pass

            except:
                pass


            
        
        return specializations


connector = Driver()
connector.connect()
specializations = connector.getSpecializations()
print(specializations)


time.sleep(10)




