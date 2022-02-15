import csv
import numpy as np
import matplotlib.pyplot as plt

csv_file = "matches.csv"
fields = []
rows = []

# reading file
with open(csv_file, 'r') as file:
    # creatign csv reader object to read contents
    csvreader = csv.reader(file)

    # extracting field names from first row
    fields = next(csvreader)
    # fields = csvreader.next()

    # extracting data from rows one by one
    for row in csvreader:
        rows.append(row)

    # finding nos. of rows
    row_cnt = csvreader.line_num -1 ## - 1 to not count the header field

# extracting season year in a list
ind = fields.index("season")
seasons = [rows[i][ind] for i in range(row_cnt)]

# extracting winner teams
ind = fields.index("winner")
winners_list = [rows[i][ind] for i in range(row_cnt)]

## replacing empty fields with 'no result'
for i in range(row_cnt): 
    if(winners_list[i] == ''):
        winners_list[i] = "No Result"

# finding distinct team names
np_win = np.array(winners_list)
unique_teams = np.unique(np_win)
# a sample dictionary to initialise the count of wins of the team in each season
teams_dict = {}
for x in unique_teams:
    teams_dict[x] = 0

# counting wins of each team per season
freq = {}
for i in range(row_cnt):
    season = seasons[i]
    team = winners_list[i]
    if season not in freq.keys():
        freq[season] = teams_dict.copy()  ## initialising from sample dictionary declared above
    freq[season][team] += 1

# # making graph
seasons_list = sorted(list(freq.keys()))
cumulative = np.array([0])

for team_name in unique_teams: # team_name is a variable that will contain different names eg: chennai super kings etc.
    # a list containg the count of wins of a particular ipl team in each district
    team_wins = np.array([freq[i][team_name] for i in seasons_list])
    plt.bar(seasons_list, team_wins, bottom = cumulative)
    cumulative = cumulative + team_wins

plt.xlabel("seasons")
plt.ylabel("Nos. of wins")
plt.title("nos. of win by each team per season")
plt.legend(unique_teams, bbox_to_anchor=(1.5,1), loc = "upper right") # to place legend outside the graph blot
plt.show()
