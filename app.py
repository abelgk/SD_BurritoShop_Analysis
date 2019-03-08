import os
from flask import Flask, jsonify, render_template
import numpy as np
import requests
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from flask import send_from_directory

# create connection to our DB
engine = create_engine("sqlite:///db/burritoShop.sqlite?check_same_thread=False")

# #################################################
# reflect our database into new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to our table
burrito_shops = Base.classes.burritoShopList
# Create our session (link) from Python to the DB
session = Session(engine)
# print(burrito_shops)

# Flask Setup
#################################################
app = Flask(__name__)

# Flask Routes
#################################################

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/shops")
def shops():
    shop_data = session.query(burrito_shops).filter(burrito_shops.Restaurant.isnot(None)) #.all()
    # print(shop_data)
    shop_data_df = pd.read_sql(shop_data.statement, session.bind).transpose()
    shop_data_dict = shop_data_df.to_dict()
    # print(shop_data_dict)
    return jsonify(shop_data_dict)
@app.route("/Overall")
def overall():

    return render_template("index2.html")

@app.route("/Meat")
def meat():

    return render_template("index_meat.html")

@app.route("/Tortilla")
def tortilla():

    return render_template("index_tortilla.html")
if __name__ == '__main__':
    app.run(port = '5000',debug=True)