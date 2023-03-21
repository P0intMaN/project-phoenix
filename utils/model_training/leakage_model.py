"""

    +--------------------------------------------+    
    | Model training for water leakage detection |
    |        with Support Vector Regressor (SVR) |
    +--------------------------------------------+

    NOTE: The input format of the training data is JSON. Refer to 
          the "dataset/json" folder to find the data we are about 
          to import for model training.
    

    Model tries to predict the flow rate on an hourly basis 
    for any given day. The attributes at play here are: 
    water pressure, day and time (0-23 in hour format).

"""

# imports
import json
import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from helper.numpy_helper import NumpyEncode

# dataset imports
datasets = [
    "monday_dataset", 
    "tuesday_dataset", 
    "wednesday_dataset", 
    "thursday_dataset", 
    "friday_dataset", 
    "saturday_dataset", 
    "sunday_dataset"
]

# list of SVRs
"""
NOTE: 7 SVR models are trained using data from 
      corresponding days
            +--------------------------+
            | svr_0  : Monday's data   |
            | svr_1  : Tuesday's data  |
            |   :    :    :            |
            | svr_6  : Sunday's data   | 
            +--------------------------+
"""
svr_machine_pool = []

# SVR training function
def train_svr(df, index):

    x = df.drop("Flow Rate", axis=1)
    y = df.iloc[:,1]

    # split the dataset for training and testing
    """
    -------------------------------------
    training dataset       : 70%
    testing dataset        : 30%
    target stratification  : disabled
    -------------------------------------
    """
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    # fit the SVR model
    regressor = SVR()
    regressor.fit(x_train, y_train)

    # adding trained svr to the pool
    svr_machine_pool.append(regressor)

    # saving model in a JSON file
    """
    We are deploying our own algorithm for JSON
    Serialization. The algorithm will capture 
    'fitted' model parameters like (weights, coeff, etc)
    and saves them in a JSON file.
    """
    attr = regressor.__dict__

    for k, v in attr.items():
        if isinstance(v, np.ndarray) and v[-1:] == '_':
            attr[k] = v.tolist()

    # saving it in a JSON file. 
    with open(f'../../project/dependencies/saved_models/saved_regressor_{index}.json', 'w') as outfile:
        json.dump(attr, outfile, cls=NumpyEncode)


# loading the datasets
dataframes = []

for name in datasets:
    dataframes.append(pd.read_json(f"../../dataset/json/{name}.json"))

# training an SVR on corresponding day's data
for index, df in enumerate(dataframes):
    train_svr(df, index)