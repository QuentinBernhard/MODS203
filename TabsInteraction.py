from selenium import webdriver

def TabsCreation(driver, url1, url2) :        # Pour l'instant que 2 onglets mais ça peut se changer facilement
    driver.get(url1)
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[1])
    #driver.get(url2)

def switchToTab(driver, indice) :
    driver.switch_to.window(driver.window_handles[indice])