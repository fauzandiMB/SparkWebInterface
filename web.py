import os
import sys
os.environ['SPARK_HOME']="usr/lib/spark"

# Append pyspark  to Python Path
sys.path.append("usr/lib/spark/python")

from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
from flask import render_template

from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark import SparkConf, SparkContext

import requests
import json
import socket

app = Flask(__name__)
	
@app.route("/", methods=["GET"])
def index():
	conf = SparkConf().setAppName("TaxiWeb")
	sc = SparkContext(conf=conf)
	model = DecisionTreeModel.load(sc, "TugasAkhir/Model/decision_tree/decision_tree_v5")
	
	return render_template("home.html")
	
@app.errorhandler(404)
def not_found(e):	
	return Response('{"detail": "The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.", "status": "404", "title": "Not Found"}', status=404, mimetype='application/json')
	
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080, debug=True)
