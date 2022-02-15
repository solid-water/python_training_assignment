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

# counting frequency of matches per season
freq = {}

for season in seasons:
    freq[season] = freq.get(season, 0) + 1

# sorting based on seasons
sorted_freq = {}
for x in sorted(freq.keys()):
    sorted_freq[x] = freq[x]


# making graph
fig = plt.figure(figsize = (7.5, 5))

plt.bar(list(sorted_freq.keys()), list(sorted_freq.values()), color = "maroon", width = 0.7)
plt.xlabel("IPL Season")
plt.ylabel("Match Count")
plt.title("IPL Matches played per season")
plt.show()
