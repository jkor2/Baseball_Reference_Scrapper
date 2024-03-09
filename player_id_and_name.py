# Baseball Reference Scrapper Player id scraper
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

# Avaiable Player Letters
player_name_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Holders to write the ecel file
player_ids = []
player_names = []

# Pull up 'allplayers' pages letter by letter
for letter in player_name_letters:
    url = "https://www.baseball-reference.com/players/%s/" % letter

    # Request url and grab content
    webpage = requests.get(url, 'html.parser')        
    soup = BeautifulSoup(webpage.content, features="lxml") 

    # Specify the id to nbe found 
    pattern_group_name = re.compile(r'div_players_')
    event_group_name = soup.find(id=pattern_group_name)

    # Specifiy the ahref link we want to split by 
    pattern = re.compile(r'/players/[a-z]/')

    # Find all tags to next grab all the names and ID's
    data = event_group_name.find_all("a")

    for i in data:
        # Append results to their respective temp_holder
        player_ids.append(re.split(pattern, i.get("href"))[1].split(".")[0])
        player_names.append(i.get_text())

# Write the excel file when complete   
df = pd.DataFrame({"player_name": player_names, "player_ids": player_ids})
df_to_excel = pd.ExcelWriter("BaseballReferencePlayerIDScrape.xlsx")
df.to_excel(df_to_excel)
df_to_excel._save()

