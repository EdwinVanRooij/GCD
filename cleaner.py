#!/usr/bin/env python3

"""
Data cleaner script to execute my data quality measures on.
"""

import pandas as pd
import numpy as np

# Read the data into a Pandas dataframe
df = pd.read_csv('Data.csv', sep=",", quotechar='"')

# Drop rows if either one of the columns contains an empty cell
df.dropna(subset=['What type of chocolate do you prefer?', 'What is your gender?'], inplace=True)

# Uppercase all cells in our two columns
df['What type of chocolate do you prefer?'] = df['What type of chocolate do you prefer?'].str.lower()
df['What is your gender?'] = df['What is your gender?'].str.lower()


def len_is_valid(param):
    """Chocolate with more than 6 characters are invalid."""
    if len(param) > 6:
        return False
    return True


# Remove all rows where either column has more than 2 words
# todo; how to make this work?
# select all records where the answer to this question passes len_is_valid's requirements

# THIS ONE DOES NOT WORK
# df = df[len_is_valid(['What type of chocolate do you prefer?'])]

# THIS ONE WORKS
# df = df[df['What type of chocolate do you prefer?'] == 'white']


print(df.loc[:, ['What type of chocolate do you prefer?', 'What is your gender?']])
