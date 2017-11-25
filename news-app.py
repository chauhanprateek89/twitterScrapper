# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 10:28:21 2017

@author: Prateek Chauhan
"""

import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)

def get_csv():
    csv_path = './static/la-riots-deaths.csv'
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        csv_list = list(reader)
    return csv_list

@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template,object_list=object_list)

if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)