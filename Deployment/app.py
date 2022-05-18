
import random as rnd
from flask import Flask, render_template ,url_for ,request
import pandas as pd

import pickle


import numpy as np
app = Flask ( __name__ )
@app.route('/')
def home():
    return render_template('home.html')
def getParameters():
    parameters = []
    parameters .append( request.form ['age'])
    parameters. append( request.form ['sex'])
    
    parameters. append( request.form ['chol'])
    parameters. append( request.form ['fbs'])
   
    parameters. append( request.form ['thal'])
    return parameters
@app.route('/predict',methods=['POST'])
def predict():
    with open(f'Heart_model.pkl', 'rb') as f:
        model = pickle.load(f)
    if request.method  == 'POST':
        parameters = getParameters()
        t =rnd.randint(0,1)
        print(parameters)
        inputFeature = np.asarray( parameters )
        # my_prediction = model.predict(inputFeature)
    return render_template ('result.html',prediction = t)
if __name__ == '__main__':
    app.run( debug = True)