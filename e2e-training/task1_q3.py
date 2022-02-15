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
    # row_cnt = csvreader.line_num ## this line not working properly for this file
    row_cnt = len(rows)

# extracting districts
ind = fields.index("district_name")
districts = [rows[i][ind] for i in range(row_cnt)]

# extracting languages
ind = fields.index("moi")
languages = [rows[i][ind] for i in range(row_cnt)]

for i in range(row_cnt): ## replacing empty fields with 'others'
    if(languages[i] == ''):
        languages[i] = "others"

# finding distinct languages
np_lang = np.array(languages)
unique_lang = np.unique(np_lang)
# a sample dictionary to initialise the count of languages in schools for each district
lang_dict = {}
for x in unique_lang:
    lang_dict[x] = 0

# counting frequency of languages per district
freq = {}
for i in range(row_cnt):
    district = districts[i]
    lang = languages[i]
    if district not in freq.keys():
        freq[district] = lang_dict.copy()  ## initialising from sample dictionary
    freq[district][lang] += 1

# # making graph
freq_districts = sorted(list(freq.keys()))
cumulative = np.array([0])

for lang_name in unique_lang: # lang_name is a variable that will contain different languages eg: kannada etc.
    # a list containg the count of schools having a particular language as moi, for each district
    lang_list = np.array([freq[i][lang_name] for i in freq_districts])
    plt.bar(freq_districts, lang_list, bottom = cumulative)
    cumulative = cumulative + lang_list

plt.xlabel("district_name")
plt.xticks(rotation = "vertical")
plt.ylabel("language_count")
plt.title("Languages spoken per District")
plt.legend(unique_lang, bbox_to_anchor=(1.2,1), loc = "upper right") # to place legend outside graph area
plt.show()
