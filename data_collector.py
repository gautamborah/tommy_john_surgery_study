from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher
from pybaseball import statcast_pitcher_spin
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from pybaseball import player_search_list
import random

injured_players_data = pd.read_csv('./player_info/MLB_Tommy_John_Surgery_List.csv')

print(injured_players_data.head())

# Iterate through injury data
MLB_TJ = (injured_players_data.query("Level == 'MLB' and Position == 'P' and Year >= 2016"))

print(list(injured_players_data.columns))
print(list(MLB_TJ.columns))
i = 0
for row in MLB_TJ.index:
  year = MLB_TJ['Year'][row]
  name = MLB_TJ['Player'][row]
  id = MLB_TJ['mlbamid'][row]
  
  player_id = str(int(id))
  print(i, player_id, name, year)
  data = statcast_pitcher(str(year-1)+'-01-01', str(year)+'-01-01', player_id=id)
  csv_file_name= './.data/'+player_id+"-"+name+"-"+str(year)+".csv"
  print("csv_file_name=", csv_file_name)  
  data.to_csv(csv_file_name)
  i+=1