# Run app by typing "uvicorn main:app --reload" in terminal
# --reload lets you hot reload your app after making changes

from fastapi import FastAPI
import psycopg2
import os
import pickle
from dotenv import load_dotenv
import pandas as pd
load_dotenv()

#Load credentials from .env
name = os.environ["DB_NAME_AWS"]
password = os.environ["DB_PW_AWS"]
host = os.environ["DB_HOST_AWS"]
user = os.environ["DB_USER_AWS"]

pg_conn = psycopg2.connect(dbname=name,
                        user=user,
                        password=password,
                        host=host
                        )


app = FastAPI()

@app.get("/")
def root():
    return {"Street": "Smarts"}


@app.post('/predict')
def predict(manufacturer:str="ford", model:str="f-150", year:int=2005):
    """
    Predict price based on year, manufacturer, model
    """
    #manufacturer = manufacturer.lower()
    # model = model.lower()

    input = pd.DataFrame({
        "year": [year],
        "manufacturer": [manufacturer],
        "model": [model]
        })

    print(input.head())
    
    test_model = pickle.load(open("random_forest_1.sav" , "rb"))
    # pred = model.predict(input)

    inputs = [year, manufacturer, model]
    
    pred = test_model.predict(input)
    print(pred)

    return {'prediction': pred[0]}

@app.post("/price")
def get_car_price(make:str="Ford", model:str="Probe", year:int=1994):
    """
    Return the predicted price of a vehicle based on Make, Model, and Year.
    """

    price = 30000 - ((2020 - year) * 2000 )

    return {"predicted_price": price}

@app.post("/carbon_emissions")
def get_co2_values(make:str="Toyota", model:str="Camry", year:int=2000):

    """
    The average vehicle emits 4.6 metric tons/year
    This function is just a placeholder
    """

    emissions = 4.6 + ((2020 - year) * .25 )

    return {"predicted_co2_emissions": emissions}

@app.post("/carbon_emissions2")
def get_co2_sql(make:str="Chevrolet", model:str="Sonic", year:int=2018):

    """
    Return the co2 value for the inputted vehicle base on make, model, and year
    """

    pg_curs = pg_conn.cursor()
    pg_curs.execute(f"SELECT AVG(co2tailpipegpm) FROM epa_vehicles_all WHERE make = '{make}' AND model = '{model}' AND year = {year};")
    value = pg_curs.fetchall()[0][0]
    pg_curs.close()

    return {"predicted_co2_sql": value}

@app.get("/carbon_emissions3")
def get_co2_sql2(make:str="Chevrolet", model:str="Sonic", year:int=2018):

    """
    Return the co2 value for the inputted vehicle base on make, model, and year
    """

    pg_curs = pg_conn.cursor()
    pg_curs.execute(f"SELECT AVG(co2tailpipegpm) FROM epa_vehicles_all WHERE make = '{make}' AND model = '{model}' AND year = {year};")
    value = pg_curs.fetchall()[0][0]
    pg_curs.close()

    return {"predicted_co2_sql": value}