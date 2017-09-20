#!/usr/bin/env python3

import numpy as np
import pandas as pd

# df = pd.read_csv('Grain-data.csv')
# print(df.shape)
# csv = np.genfromtxt('Grain-data.csv', delimiter=";")

import csv

row_count = 0
newlines = 0

for row in csv.reader(open('Grain-data.csv'), delimiter=';'):
    print("Land: {}, row: {}".format(row['Landgrabbed'], row))
    # row_count += 1
    # if row.count('\n'):
    #     newlines += 1

    with open("test.txt", "a") as myfile:
        myfile.write(row)

print("row_count:", row_count)
print("newlines:", newlines)
