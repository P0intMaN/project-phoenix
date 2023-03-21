"""

    +---------------------------------------------+
    | Python script to convert csv dataset to JSON|
    +                                             +
    | eg:    x_dataset.csv --> x_dataset.json     |
    +---------------------------------------------+

"""

# imports
import pandas as pd

# dataset list
datasets = [
    "monday_dataset",
    "tuesday_dataset",
    "wednesday_dataset",
    "thursday_dataset",
    "friday_dataset",
    "saturday_dataset",
    "sunday_dataset",
    "water_quality"
]

for d in datasets:
    file = pd.read_csv(f'../dataset/csv/{d}.csv')
    json_file = file.to_json(f'../dataset/json/{d}.json')
