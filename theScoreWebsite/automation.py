import time
import types
import typing
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Automation(webdriver.Chrome):
   
  def __init__(self, teardown=False):
    super(Automation, self).__init__
    self.teardown = teardown # teardown is basically condition to quit the automation. Automation exit automatically when finish 
  
  def __exit__(self, exec_type, exec_val, exec_tb):
    if self.teardown:
      self.quit()
  
  #Function directs to the home page
  def home_page(self):
    ##Important ln 7-9 for chrome testing
    self.options = webdriver.ChromeOptions()
    self.options.add_experimental_option("detach", True)
    self.driver = webdriver.Chrome(options=self.options)
    
    self.driver.get("https://www.thescore.com/")
    self.driver.maximize_window()
  
  #Function directs tot the sport page. Atm it is four: mlb, nba, nlh, nfl
  def sport_page(self, sport=None):
    
    #xpath  "//tagname[@Attribute=’value’]""
    nbaLink = self.driver.find_element(By.CSS_SELECTOR, f"a[href='/{sport}/news']")
    nbaLink.click() ##goes to the nba link

    #Wait so the driver gets the updated url
    time.sleep(2)
  
  
  #Function gets the games that are upcoming  
  def get_Games(self):
    
    tickerContent = self.driver.find_element(By.CSS_SELECTOR, 'div[style="height: 76px;"]')

    tickerContentWrapper = tickerContent.find_element(By.XPATH, '//*[@id="main-content"]/div[3]/div/div[3]/div/div/div[2]/div')

    teamNames = tickerContentWrapper.find_elements(By.CSS_SELECTOR, 'span[class="jsx-627093717 teamName"]')
    gameDates = tickerContentWrapper.find_elements(By.CSS_SELECTOR, 'div[class="jsx-627093717 gameInfo"]')
    gameTimes = tickerContentWrapper.find_elements(By.CSS_SELECTOR, 'div[class="jsx-627093717 gameInfo dark"]')


    i = 0
    x = 0 #number of games

    if len(teamNames) == 2:
      if (gameTimes == []):
        print(f'{x+1}. {teamNames[i].text} vs {teamNames[i+1].text} | Game is currently live or is finished')
      else:
        print(f"{x+1}. {teamNames[i].text} vs {teamNames[i+1].text} | {gameDates[x].text} | {gameTimes[x].text}")
      return

    while x < (int(len(teamNames)/2)):
      
      if (x > len(gameTimes) - 1):
        print(f'{x+1}. {teamNames[i].text} vs {teamNames[i+1].text} | Game is currently live or is finished')
      else:
        print(f"{x+1}. {teamNames[i].text} vs {teamNames[i+1].text} | {gameDates[x].text} | {gameTimes[x].text}")
        
      i += 2
      x += 1
      
    
