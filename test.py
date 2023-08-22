import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def league_table():

    url = 'https://www.espn.com/soccer/standings/_/league/eng.1'
    headers = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text,  "html.parser")
    print(page)
    table= soup.find("table", class_="ssrcss-14j0ip6-Table e3bga5w5")

    for i in table.find_all('th'):
        title = i.text
        headers.append(title)
    league_table = pd.DataFrame(columns = headers)
    for j in table.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(league_table)
        league_table.loc[length] = row
    league_table.drop(["Form, Last 6 games, Oldest first"], axis=1, inplace=True)
    return league_table

league_table()