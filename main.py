import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

##Important ln 7-9 for chrome testing
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.thescore.com/")

driver.maximize_window()

time.sleep(2)
navigationBar = driver.find_element(By.CLASS_NAME,"DesktopMenu__leagueMenu--1g2I_")

#xpath  "//tagname[@Attribute=’value’]""
nbaLink = navigationBar.find_element(By.XPATH, "//a[@href='/nba/news']" )
nbaLink.click()

upcomingGames = nbaLink.find_element(By.CLASS_NAME, "jsx-507102810 tickerContent")

for e in upcomingGames:
  print ("YERR")

