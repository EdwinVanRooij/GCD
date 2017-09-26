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

projected_investment_new = 'Projected investment (US$ millions)'  # 7

count = 0


def clean_cell(cell):
    # Remove whitespace
    # result = "".join(cell.split())
    result = cell.strip()

    # If result is now empty, replace with some text
    if not result:
        return "Missing"

    return result


def transform_investment(investment):
    # Don't do anything if the value is missing
    if investment == "Missing":
        return investment

    # Do transformation
    investment = investment[3:]  # removes first three characters
    investment = investment.split(' ', 1)[0]  # removes everything starting at the first space

    print(investment)
    return investment


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
            projected_investment_new,
            status_of_deal,
            summary,
        ])
        count += 1

        # Loop over every record in the dirty data file
        for record in reader:
            # Clean the cell
            writer.writerow([
                clean_cell(record[landgrabbed]),
                clean_cell(record[landgrabber]),
                clean_cell(record[base]),
                clean_cell(record[sector]),
                clean_cell(record[hectares]),
                clean_cell(record[production]),
                clean_cell(record[projected_investment]),
                transform_investment(clean_cell(record[projected_investment])),
                clean_cell(record[status_of_deal]),
                clean_cell(record[summary]),
            ])
            count += 1

print("Rows written:", count)

# I have used regular expressions in past week's assignment, and used trim & substitute formulas as well.
