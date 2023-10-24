from theScoreWebsite.automation import Automation

with Automation() as bot:
  bot.home_page()
  bot.sport_page("mlb") #Options: nfl, nba, mlb, nhl
  bot.get_Games()
