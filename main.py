# Run app by typing "uvicorn main:app --reload" in terminal
# --reload lets you hot reload your app after making changes

from fastapi import FastAPI
import psycopg2
import os
import pickle
from dotenv import load_dotenv
import pandas as pd
from fuzzywuzzy import fuzz, process
from joblib import load
import requests
import numpy as np

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
## Curson is always open
pg_curs = pg_conn.cursor()

app = FastAPI()

# Load in slimmed random forest pickled model
#test_model = pickle.load(open("random_forest_1.sav" , "rb"))
test_model = load("random_forest_2.joblib")

# Load the craigslist cleaned data
df_cl = pd.read_csv("https://raw.githubusercontent.com/Lambda-School-Labs/street-smarts-ds/master/data/craigslist_df_cleaned2.csv")
# List of unique CL cars
cl_models = sorted(df_cl.model.unique())

@app.get("/")
def root():
    return {"Street": "Smarts",
            "Version": "Lite",
            "API": "/docs"}


@app.post('/predict')
def predict(make:str="Ford", model:str="F150 Pickup 4WD", year:int=2005):
    """
    Predict price based on year, manufacturer, model
    """
    manufacturer = make
    manufacturer = manufacturer.lower()
    model_lower = model.lower()
    def match_models(sample_model):
        '''
        This function takes in a given model from the EPA dataset and
        uses the Fuzzy Wuzzy library to match the input string to the closest
        string in the Craigslist dataset.
        '''
        model_ratios = []
        for car in cl_models:
            model_ratios.append(fuzz.ratio(sample_model, car))
        max_match = max(model_ratios)
        index_of_match = model_ratios.index(max_match)
        return cl_models[index_of_match]
    # Call the function to get the CL equivalent car
    model_fz = match_models(model_lower)
    
    input = pd.DataFrame({
        "year": [year],
        "manufacturer": [manufacturer],
        "model": [model_fz]
        })
    
    pred = test_model.predict(input)

    car_price_prediction = pred[0]
    
    '''
     still need:

     federal state local incentives
     state sales tax
     '''

   
    ## Constant values
    ## These can be user inputs in a later release canvas

    miles_per_year = 15000
    num_years = 5
    mpg = 25
    gas_cost = 3
    electric_cost = .12
    maintenance_cost_per_year = 1000

    # Query the database for combined mpg
    pg_curs.execute(f"select AVG(comb08) FROM epa_vehicles_all WHERE make = '{make}' and model = '{model}' and year = '{year}';")
    mpg_combined = pg_curs.fetchall()[0][0]

    # Query the database for combined mpg
    pg_curs.execute(f"SELECT AVG(co2tailpipegpm) FROM epa_vehicles_all WHERE make = '{make}' AND model = '{model}' AND year = {year};")
    co2_grams_per_mile = pg_curs.fetchall()[0][0]

    ## CO2 over a X year period
    ## Units are now in kilograms
    co2_over_time = co2_grams_per_mile * miles_per_year  * num_years / 1000

    # Outputs of the route 
    fuel_cost = (miles_per_year / mpg_combined * gas_cost * num_years)

    maintenance_cost = maintenance_cost_per_year * num_years

    five_year_cost_to_own = (
    
    car_price_prediction +

    ## Need to query the EPA database to determine fuel type

    ## If gas:
    fuel_cost +
    
    ## IF electric
    #(miles_per_year / mpg * electric_cost * num_years) +

    ## Eventually, we could break out electric vs gas maintenance numbers
    maintenance_cost
    )
    ## Number of kgs of CO2 absorbed by one tree per year
    tree_absorption = 21.7724
    number_of_trees_to_offset = co2_over_time/(tree_absorption*num_years)
    
    #### Images of Selected Car

    def test_get_list_urls_check_status_code_equals_200(url):
        response = requests.get(url)
        if response.status_code == 200:
            url = url
        else:
            return np.NaN
        return url
    def fetch_img(car_model, year):
        """
        Get from sample input car to return the url. If none found,
        check next and previous year. If none available, give none found image
        """
        df_models = df_cl[df_cl['model'] == car_model]
        df_models_at_year = df_models[df_models['year'] == year ]
        index_of_model_year = df_models_at_year.index[0:10]

        list_urls = list(df_cl['image_url'][index_of_model_year])
        ##for loop
        list_nan_urls = [test_get_list_urls_check_status_code_equals_200(x) for x in list_urls]
        print(list_nan_urls)
        clean_list_urls = [x for x in list_nan_urls if x is not np.NaN]
        print(clean_list_urls, 'current year')            

        # Check if there are any cars in the current year, else check next year
        if len(clean_list_urls) == 0:
            df_models_at_year = df_models[df_models['year'] == (year + 1)]
            index_of_model_year = df_models_at_year.index[0:10]
            list_urls = list(df_cl['image_url'][index_of_model_year])
            ##for loop
            list_nan_urls = [test_get_list_urls_check_status_code_equals_200(x) for x in list_urls]
            print(list_nan_urls)
            clean_list_urls = [x for x in list_nan_urls if x is not np.NaN]
            print(clean_list_urls, 'next year')

            # if there are any cars in the current year, else check PREV year
            if len(clean_list_urls) == 0:
                df_models_at_year = df_models[df_models['year'] == (year - 1)]
                index_of_model_year = df_models_at_year.index[0:10]
                list_urls = list(df_cl['image_url'][index_of_model_year])
                #print('No cars in specified year, trying the previous year')  
                ##for loop
                list_nan_urls = [test_get_list_urls_check_status_code_equals_200(x) for x in list_urls]
                print(list_nan_urls)
                clean_list_urls = [x for x in list_nan_urls if x is not np.NaN]
                print(clean_list_urls, 'previous year')

                if len(clean_list_urls) == 0:
                    return ['https://raw.githubusercontent.com/Lambda-School-Labs/street-smarts-ds/master/data/noImage_large.png']
                return clean_list_urls  

            #print('No cars in specified year, trying the next year')
            return clean_list_urls

        return clean_list_urls
      
    list_of_imgs = fetch_img(model_fz, year)

    return {"car_price_prediction": car_price_prediction.round(2),
            "fuel_cost": round(fuel_cost, 2),
            "maintenance_cost": maintenance_cost,
            "five_year_cost_to_own": five_year_cost_to_own.round(2),
            "co2_five_year_kgs": round(co2_over_time, 2), 
            "number_of_trees_to_offset": round(number_of_trees_to_offset, 0)}

@app.post("/carbon_emissions2")
def get_co2_sql(make:str="Chevrolet", model:str="Sonic", year:int=2018):

    """
    Return the co2 value for the inputted vehicle base on make, model, and year
    """

 
    pg_curs.execute(f"SELECT AVG(co2tailpipegpm) FROM epa_vehicles_all WHERE make = '{make}' AND model = '{model}' AND year = {year};")
    value = pg_curs.fetchall()[0][0]
    #pg_curs.close()

    return {"predicted_co2_sql": value}
