from flask import Flask,request  # From 'flask' module import 'Flask' class
app = Flask(__name__)    # Construct an instance of Flask class for our webapp
import cv2 as cv
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
import h5py
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')  
@cross_origin()
def main():
    """Say hello"""
    print("hi")
    return "Hello, jimmy!"
@app.route('/predict/', methods = ['GET'])
@cross_origin()
def files():
    with open("files.txt","w+") as r:
        r.write("hello python")
    g=""
    with open("files.txt","r") as r:
     g=g+r.read()
     
    return g 
@app.route('/index/',methods=['Get'])
def home():
   return render_template('view.html')
if __name__ == '__main__':
    app.run()     
