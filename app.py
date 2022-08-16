# -*- coding: utf-8 -*-
"""
Created on 14/09/2022 

@author: 
"""


# coding: utf-8

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn import metrics
#from flask import Flask, request, render_template
import pickle

# ad new
import numpy as np
from flask import Flask, request, jsonify, render_template
import datetime

app = Flask("__name__")


q = ""

model = pickle.load(open('model.pkl', 'rb'))
features = []

@app.route("/")
def loadPage():
	return render_template('home.html', query="")


@app.route("/", methods=['POST'])
def predict():
    
    '''
    For rendering results on HTML GUI
    '''
    features = [x for x in request.form.values()]
    print(features)
    date_format = datetime.datetime.strptime(features[-1], "%Y-%m-%d")
    features[-1] = datetime.datetime.timestamp(date_format)
    print(features[-1])
    final_features = [np.array(features[:-1])]
    print(final_features)
    prediction = model.predict(final_features)

    output = prediction

    return render_template('index.html', prediction_text='The probability that this transaction is fraudulent is {}'.format(output))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

