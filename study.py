from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher
from pybaseball import statcast_pitcher_spin
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from pybaseball import player_search_list
import random

injury_data = pd.read_csv('./.data/players/MLB_Tommy_John_Surgery_List.csv')

print(injury_data.head())

healthy = {}
unhealthy = {}

def value_gen(player_id, name, TJ, year):
  #   data = statcast_pitcher(str(year-1)+'-01-01', str(year)+'-01-01', player_id=player_id)
  id = str(int(player_id))
  print(id, name, year)
  csv_file_name= './.data/'+id+"-"+name+"-"+str(year)+".csv"
  print("csv_file_name=", csv_file_name)  
  data = pd.read_csv(csv_file_name)  
  Fastballs = data.loc[data['pitch_type'].isin(['FF', 'SI'])]
  FF = data.loc[data['pitch_type'].isin(['FF'])]
  SI = data.loc[data['pitch_type'].isin(['SI'])]
  FC = data.loc[data['pitch_type'].isin(['FC'])]
  OFF = data.loc[~data['pitch_type'].isin(['FF', 'SI'])]
  CH = data.loc[data['pitch_type'].isin(['CH'])]
  SPL = data.loc[data['pitch_type'].isin(['FS', 'FO'])]
  SL = data.loc[data['pitch_type'].isin(['SL', 'SV', 'ST'])]
  Sweep = data.loc[data['pitch_type'].isin(['ST'])]
  CU = data.loc[data['pitch_type'].isin(['CU', 'KC', 'CS'])]
  mean_veloFF = FF['release_speed'].mean()
  mean_veloOFF = OFF['release_spin_rate'].mean()
  mean_release = data['release_pos_z'].mean()
  mean_spinFF = FF['release_spin_rate'].mean()
  mean_spinOFF = OFF['release_spin_rate'].mean()
  if TJ == True:
    unhealthy[player_id] = [name, data, mean_veloFF, mean_veloOFF, mean_release, mean_spinFF, mean_spinOFF, Fastballs, FF, SI, FC, CH, SPL, SL, Sweep, CU, OFF]
  elif TJ == False:
    healthy[player_id] = [name, data, mean_veloFF, mean_veloOFF, mean_release, mean_spinFF, mean_spinOFF, Fastballs, FF, SI, FC, CH, SPL, SL, Sweep, CU, OFF]
  return data, mean_veloFF, mean_veloOFF, mean_release, mean_spinFF, mean_spinOFF


# Iterate through injury data
# MLB_TJ = (injury_data.query("Level == 'MLB' and Position == 'P' and Year >= 2016"))
#/Users/gautamborah/tjs/tommy_john_surgery_study/.data/669622-Anthony Bender-2022.csv
data, mean_veloFF, mean_veloOFF, mean_release, mean_spinFF, mean_spinOFF = value_gen(669622, "Anthony Bender", True, 2022)

print(data.head())

#/Users/gautamborah/tjs/tommy_john_surgery_study/.data/681810-Austin Warren-2023.csv
data, mean_veloFF, mean_veloOFF, mean_release, mean_spinFF, mean_spinOFF = value_gen(681810, "Austin Warren", True, 2023)

print(data.head())