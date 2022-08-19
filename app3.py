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

model = pickle.load(open('model.sav', 'rb'))
features = []

@app.route("/")
def loadPage():
	#return render_template('home.html', query="")
	return render_template('index.html', query="")


@app.route("/", methods=['POST'])
def predict():
    
    '''
    For rendering results on HTML GUI
    '''
    
    inputQuery1 = request.form['Amount']
    #print(inputQuery1)
    inputQuery2 = request.form['gender']
    print(inputQuery2)
    inputQuery3 = request.form['Age']
    inputQuery3 = request.form['zip']
    print(inputQuery3)
    inputQuery4 = request.form['dob']
    print(inputQuery4)
    inputQuery5 = request.form['CATEGORY']
    print(inputQuery5)
    
    
    model = pickle.load(open("model.sav", "rb"))
    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5]]
    new_df = pd.DataFrame(data, columns = ['Amount', 'gender', 'Age', 'dob', 'CATEGORY'])
    
    single = model.predict(new_df)
    probablity = model.predict_proba(new_df)[:,1]
    
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
    print(output)

    return render_template('index.html', prediction_text='The probability that this transaction is fraudulent is {}'.format(output))
    '''
    
   
   
    return render_template('index.html', )



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)


