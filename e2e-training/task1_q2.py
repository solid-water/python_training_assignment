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

# extracting school category
ind = fields.index("cat")
category = [rows[i][ind] for i in range(row_cnt)]

# finding the distinct school categories
np_cat = np.array(category)
unique_cat = np.unique(np_cat)
# a sample dictionary to initialise the count of different categories for each district
cat_dict = {}
for x in unique_cat:
    cat_dict[x] = 0

# counting frequency of school per district
freq = {}
for i in range(row_cnt):
    district = districts[i]
    s_type = category[i]
    if district not in freq.keys():
        freq[district] = cat_dict.copy()  ## initialising from sample dictionary
    freq[district][s_type] += 1

# # making graph
freq_districts = sorted(list(freq.keys()))
cumulative = np.array([0]) # for plotting of stacked bar graph

for category_name in unique_cat: # category name is a variable that will contain school categories eg: lower primary, secondary etc.
    # a list containg the count of a particular school category for each district
    c_list = np.array([freq[i][category_name] for i in freq_districts]) 
    plt.bar(freq_districts, c_list, bottom = cumulative)
    cumulative = cumulative + c_list

### the above code block is a generalised version to below commented code
'''# lower_prim = np.array([freq[i]['Lower Primary'] for i in freq_districts])
# model_prim = np.array([freq[i]['Model Primary'] for i in freq_districts])
# secondary_ = np.array([freq[i]['Secondary'] for i in freq_districts])
# upper_prim = np.array([freq[i]['Upper Primary'] for i in freq_districts])

# plt.bar(freq_districts, lower_prim, color = "red", width = 0.8)
# plt.bar(freq_districts, model_prim, bottom = lower_prim, color = "blue", width = 0.8)
# plt.bar(freq_districts, secondary_, bottom = lower_prim + model_prim, color = "green", width = 0.8)
# plt.bar(freq_districts, upper_prim, bottom = lower_prim + model_prim + secondary_, color = "yellow", width = 0.8)
'''
plt.xlabel("district_name")
plt.xticks(rotation = "vertical")
plt.ylabel("school_category_count")
plt.title("School Category per District")
plt.legend(unique_cat)
plt.show()
