"""

    +------------------------------------------------+    
    | Entire backend logic sits in this python file. |
    | Responsible for:                               |
    |  * handling requets                            |
    |  * getting field inputs form the portal        |
    |  * hitting local storage                       |
    |  * invoking saved machine learning models      |
    |  * server-side rendering of html pages         |
    +------------------------------------------------+

"""

# imports
from flask import render_template
from app import flask_app
import pickle
from flask import request
import json
import codecs
import numpy as np
from sklearn import svm
from sklearn.svm import SVR


#### helper functions
def params_from_json(filename):
    obj_text = codecs.open(filename, 'r', encoding='utf-8').read()
    params = json.loads(obj_text)

    return params


def attr_from_json(filename):
    obj_text = codecs.open(filename, 'r', encoding='utf-8').read()
    attributes = json.loads(obj_text)

    return attributes


# flask routes
"""
NOTE:   Each route is responsible for handling an endpoint.
        The logic which follows after a request hits an 
        endpoint should be written within a route.
        Furthermore, we can put restrictions on the type
        of requests hitting an endpoint.
"""
@flask_app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


# route for handling a request to
# '/predict' endpoint
@flask_app.route("/predict")
def prediction():
    classifier = svm.SVC(kernel='rbf')

    # setting the saved trained values from stored JSON file
    svc_attr = json.load(open('../dependencies/saved_models/water_quality_svm.json'))
    svc_attr.pop('feature_names_in_', None)

    for k, v in svc_attr.items():
        if isinstance(v, list):
            setattr(classifier, k, np.array(v))
        else:
            setattr(classifier, k, v)

    # getting the data from form submission
    ph = float(request.args.get("ph"))
    hardness = float(request.args.get("hardness"))
    temperature = float(request.args.get("temperature"))
    turbidity = float(request.args.get("turbidity"))
    day = float(request.args.get("day"))
    time = float(request.args.get("time"))
    fr = float(request.args.get("fr"))
    wp = float(request.args.get("wp"))

    # making the prediction for water quality 
    # from the data received from form
    quality_prediction = str(classifier.predict([[ph, hardness, turbidity, temperature]]))
    flow_rate_prediction = ""

    if day == 0:
        generic_svm = SVR(kernel='rbf')

        # setting the saved trained values from stored JSON file
        attr = json.load(open('../dependencies/saved_models/saved_regressor_0.json'))

        for k, v in attr.items():
            if isinstance(v, list):
                setattr(generic_svm, k, np.array(v))
            else:
                setattr(generic_svm, k, v)

        flow_rate_prediction = float(generic_svm.predict([[time, wp]]))

    elif day == 1:
        generic_svm = SVR(kernel='rbf')

        # setting the saved trained values from stored JSON file
        attr = json.load(open('../dependencies/saved_models/saved_regressor_1.json'))

        for k, v in attr.items():
            if isinstance(v, list):
                setattr(generic_svm, k, np.array(v))
            else:
                setattr(generic_svm, k, v)

        flow_rate_prediction = float(generic_svm.predict([[time, wp]]))

    elif day == 2:
        generic_svm = SVR(kernel='rbf')

        # setting the saved trained values from stored JSON file
        attr = json.load(open('../dependencies/saved_models/saved_regressor_2.json'))

        for k, v in attr.items():
            if isinstance(v, list):
                setattr(generic_svm, k, np.array(v))
            else:
                setattr(generic_svm, k, v)

        flow_rate_prediction = float(generic_svm.predict([[time, wp]]))

    elif day == 3:
        generic_svm = SVR(kernel='rbf')

        # setting the saved trained values from stored JSON file
        attr = json.load(open('../dependencies/saved_models/saved_regressor_3.json'))

        for k, v in attr.items():
            if isinstance(v, list):
                setattr(generic_svm, k, np.array(v))
            else:
                setattr(generic_svm, k, v)

        flow_rate_prediction = float(generic_svm.predict([[time, wp]]))

    elif day == 4:
        generic_svm = SVR(kernel='rbf')

        # setting the saved trained values from stored JSON file
        attr = json.load(open('../dependencies/saved_models/saved_regressor_4.json'))

        for k, v in attr.items():
            if isinstance(v, list):
                setattr(generic_svm, k, np.array(v))
            else:
                setattr(generic_svm, k, v)

        flow_rate_prediction = float(generic_svm.predict([[time, wp]]))

    elif day == 5:
        generic_svm = SVR(kernel='rbf')

        # setting the saved trained values from stored JSON file
        attr = json.load(open('../dependencies/saved_models/saved_regressor_5.json'))

        for k, v in attr.items():
            if isinstance(v, list):
                setattr(generic_svm, k, np.array(v))
            else:
                setattr(generic_svm, k, v)

        flow_rate_prediction = float(generic_svm.predict([[time, wp]]))

    elif day == 6:
        generic_svm = SVR(kernel='rbf')

        # setting the saved trained values from stored JSON file
        attr = json.load(open('../dependencies/saved_models/saved_regressor_6.json'))

        for k, v in attr.items():
            if isinstance(v, list):
                setattr(generic_svm, k, np.array(v))
            else:
                setattr(generic_svm, k, v)

        flow_rate_prediction = float(generic_svm.predict([[time, wp]]))
    
    flow_rate_prediction += 0.3
    if flow_rate_prediction < fr:
        flow_rate_prediction = "1"
    else:
        flow_rate_prediction = "0"
        print(quality_prediction, flow_rate_prediction)
    return str(quality_prediction + " " + flow_rate_prediction)
