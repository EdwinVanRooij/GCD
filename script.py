#!/usr/bin/env python3

import numpy as np
import pandas as pd

# df = pd.read_csv('Grain-data.csv')
# print(df.shape)
# csv = np.genfromtxt('Grain-data.csv', delimiter=";")

import csv
import string

# Header rows legend
landgrabbed = 'Landgrabbed'  # 1
landgrabber = 'Landgrabber'  # 2
base = 'Base'  # 3
sector = 'Sector'  # 4
hectares = 'Hectares'  # 5
production = 'Production'  # 6
projected_investment = 'Projected investment'  # 7
status_of_deal = 'Status of deal'  # 8
summary = 'Summary'  # 9

count = 0


def remove_whitespace(param):
    return "".join(param.split())


# Open the dirty data file
with open("Data-python.csv") as file_in:
    # Read the records in a dictionary format
    reader = csv.DictReader(file_in, delimiter=";")

    # Create a new clean file
    with open("Edited-data-python.csv", "w", newline='') as file_out:
        # Create a writer
        writer = csv.writer(file_out, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Write the header row first
        writer.writerow([
            landgrabbed,
            landgrabber,
            base,
            sector,
            hectares,
            production,
            projected_investment,
            status_of_deal,
            summary,
        ])
        count += 1

        # Loop over every record in the dirty data file
        for record in reader:
            # Write a row without whitespace
            writer.writerow([
                remove_whitespace(record[landgrabbed]),
                remove_whitespace(record[landgrabber]),
                remove_whitespace(record[base]),
                remove_whitespace(record[sector]),
                remove_whitespace(record[hectares]),
                remove_whitespace(record[production]),
                remove_whitespace(record[projected_investment]),
                remove_whitespace(record[status_of_deal]),
                remove_whitespace(record[summary]),
            ])
            count += 1

print("Rows written:", count)
