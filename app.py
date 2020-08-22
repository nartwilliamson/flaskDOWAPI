from flask import Flask, jsonify, request

from flask_cors import CORS


import numpy as np
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

tickerList2 = ['MMM', 'AXP', 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'KO', 'DOW', 'XOM' , 'GS', 'HD', 'IBM', 'INTC','JNJ','JPM', 'MCD', 'MRK', 'MSFT', 'NKE', 'PFE', 'PG', 'TRV', 'UNH', 'UTX','VZ','V', 'WMT', 'WBA', 'DIS']
dowFrame = pd.read_pickle("dowDF.pkl")
stockDict = dowFrame.to_dict('records')

tempList = []
for name in tickerList2:
    for p in stockDict:
        tempList.append({"Value" : (p[name]), "Date": p['DateColumn'], "Ticker":name})

#jsonList = json.dumps(tempList)

@app.route('/') 
def get_stores():
    return jsonify(tempList)

app.run(port=5000, debug=True)

