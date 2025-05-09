import pandas as pd
import numpy as np


players_df = pd.read_csv('data.csv')

ranks = ['Best Team', 'Second Best', 'Third Best', '4th', '5th', '6th', 'Third Worst', 'Second Worst', 'Worst Team']
players_df.index = ranks
print('\nThese are the projections for the 9 best MLB Teams and their respective players:')
print()
print(players_df)
print()
# print(players_df.loc['Best Team', 'Teams']) ## should print out Dodgers    WORKS

print('*****************************************************************************************\n')

for index, row in players_df.iterrows():
    for index2, row2 in players_df.iterrows():
        if (players_df.loc[index, 'Teams'] == 'Dodgers') and (index2 == 'Worst Team'):         ## brings Dodgers to the bottom
            temp = players_df.loc[index2]               ## Stores Astros value
            players_df.loc[index2] = players_df.loc[index]
            players_df.loc[index] = temp

for index, row in players_df.iterrows():
    for index2, row2 in players_df.iterrows():
        if (index == 'Best Team') and (players_df.loc[index2, 'Best Player'] == 'Christian Carrington'):         ## brings team with Christian Carrington to the top
            temp = players_df.loc[index]               ## Stores Astros value
            players_df.loc[index] = players_df.loc[index2]
            players_df.loc[index2] = temp

print('These are the true facts of life for the MLB:\n')
print(players_df) 



