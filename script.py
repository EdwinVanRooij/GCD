#!/usr/bin/env python3

import numpy as np
import pandas as pd

# df = pd.read_csv('Grain-data.csv')
# print(df.shape)
# csv = np.genfromtxt('Grain-data.csv', delimiter=";")

import csv

with open('Grain-data.csv') as file:
    reader = csv.reader(file)

    row_count = 0
    newlines = 0
    for row in reader:
        print("Row: ", row)
        row_count += 1
        if row.count('\n'):
            newlines += 1
    print("row_count:", row_count)
    print("newlines:", newlines)
