"""

    +--------------------------------------------+    
    | Model training for water quality detection |
    |          with Support Vector Machine (SVM) |
    +--------------------------------------------+

    NOTE: The training data is sourced from Kaggle. But, if there 
          is a need to reproduce a custom dataset, one may follow 
          the below format as is:

          {
            "ph":          { "0": 3, "2": 7,       ..., "n": n },
            "Hardness":    { "0": 123, "1": 23.23, ..., "n": n },
            "Turbidity":   { "0": 3, "1": 4,       ... ,"n": n },
            "Temperature": { "0": 3, "1": 4,       ... ,"n": n },
            "Quality:"     { "0": 0, "1": 1,       ... ,"n": 0 }
          }

                        Data format       : JSON
                        File extension    : .json
                        File destination  : dataset/json/
    

    Model tries to predict the Potability (Quality) of water given a 
    set of attributes: pH, turbidity, temperature, hardness.

"""

# imports
import json
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from helper.numpy_helper import NumpyEncode

# load dataset
dataset = pd.read_json('../../dataset/json/water_quality.json')

# selecting features
X = dataset[['ph', 'Hardness', 'Turbidity', 'Temperature']]

# target : Potability
y = dataset.iloc[:, -2]

# split the dataset for training and testing
"""
-------------------------------------
   training dataset       : 80%
   testing dataset        : 20%
   target stratification  : enabled
-------------------------------------
"""
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2, stratify=y)

# training with SVM
classifier = svm.SVC(kernel='rbf')
classifier.fit(x_train, y_train)

# prediction
pred = classifier.predict(x_test)

# accuracy checking
"""
NOTE: A total of 10 experimental trials were 
      conducted to evaluate the model's performance, 
      and the following statistical metrics of 
      accuracy were recorded:
            +-------------------+
            | Lowest  : 95.533% |
            | Best    : 97.392% |
            | Average : 96.774% |
            +-------------------+
"""
print(f"Model Accuracy: {accuracy_score(pred, y_test) * 100}%")

# saving model in a JSON file
"""
Capturing the 'fitted' model parameters and saving
them in a JSON file. This file will later be loaded
by the web application for prediction.
"""
attr = classifier.__dict__

for k, v in attr.items():
    if isinstance(v, np.ndarray) and v[-1:] == '_':
        attr[k] = v.tolist()

with open(f'../../project/dependencies/saved_models/water_quality_svm.json', 'w') as outfile:
        json.dump(attr, outfile, cls=NumpyEncode)
