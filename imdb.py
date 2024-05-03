import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.common.by import By  
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

class WebLocators:
   
   def __init__(self):
       self.NameLocator = "name-text-input"
       self.BirthLocator ="birth-date-start-input"
       self.birthdayLocator = "birthday-input"
       self.buttonlocator = '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button'
       self.Oscarlocator ='//*[@id="accordion-item-awardsAccordion"]/div/section/button'
       self.awardlocator = '//*[@id="accordion-item-pageTopicsAccordion"]/div/div/section/button[1]'
       self.Femalelocator = '//*[@id="accordion-item-genderIdentityAccordion"]/div/section/button[2]'
       self.Includelocator = '//input[@aria-label="Include" and @data-testid="include-adult-names"]'
       self.resultlocator = '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button'
       self.menulocator = '//*[@id="imdbHeader-navDrawerOpen"]/span'
       self.clearlocator = '//*[@id="imdbHeader"]/div[2]/aside[1]/div/div[1]/label'
       self.SearchLocator = "q"
       self.enterlocator = '//*[@id="suggestion-search-button"]'

   def enterText(self, driver, value, textValue):
       element=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, value)))
       element.send_keys(textValue)
   def clickButton(self,driver, value):
       element=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, value)))
       element.click()
   
class WebData:
   
   def __init__(self):
       self.url = "https://www.imdb.com/search/name/"
       self.Name = "Aundrey"
       self.Birth = "20/03/2001"
       self.birthday = "20/03"
       self.Search = "Aundrey"

class imdb:

   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):
       self.driver.get(WebData().url)
       self.driver.maximize_window()
       self.wait = WebDriverWait(self.driver, 10)

   def quit(self):
       self.driver.quit()

   def imdb1(self):

    try:
       self.boot()
       WebLocators().clickButton(self.driver, WebLocators().buttonlocator)
       WebLocators().enterText(self.driver, WebLocators().NameLocator, WebData().Name)
       WebLocators().enterText(self.driver, WebLocators().BirthLocator, WebData().Birth)
       WebLocators().clickButton(self.driver, WebLocators().resultlocator)
       time.sleep(10)
       WebLocators().clickButton(self.driver, WebLocators().menulocator)
       time.sleep(10)
       WebLocators().clickButton(self.driver,WebLocators().clearlocator)
       time.sleep(10)
       WebLocators().enterText(self.driver, WebLocators().SearchLocator, WebData().Search)
       WebLocators().clickButton(self.driver, WebLocators().enterlocator)
    except NoSuchElementException as e:
        print("Error!")        
    finally:
        self.quit()         
    
obj = imdb()
obj.imdb1()
















































   
    
    
   

    
       
   
    





    
   

    

       

