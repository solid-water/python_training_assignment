import csv
import numpy as np
import matplotlib.pyplot as plt

csv_file = "primaryschool.csv"
fields = []
rows = []

# reading file
with open(csv_file, 'r') as file:
    # creatign csv reader object to read contents
    csvreader = csv.reader(file)

    # extracting field names from first row
    fields = next(csvreader)

    # extracting data from rows one by one
    for row in csvreader:
        rows.append(row)

    # finding nos. of rows
    # row_cnt = csvreader.line_num -1 ## this line not working properly for this file
    row_cnt = len(rows)

# extracting districts
ind = fields.index("district_name")
districts = [rows[i][ind] for i in range(row_cnt)]

# counting frequency of districts to get the frequency of school per district
freq = {}

for district in districts:
    freq[district] = freq.get(district, 0) + 1

# making graph
fig = plt.figure(figsize = (7.5, 5))

plt.bar(list(freq.keys()), list(freq.values()), color = "maroon", width = 0.7)
plt.xlabel("district_name")
plt.xticks(rotation = "vertical")
plt.ylabel("school_count")
plt.title("Schools per District")
plt.show()
