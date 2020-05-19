import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

#Load credentials from .env
name = os.environ["DB_NAME_AWS"]
password = os.environ["DB_PW_AWS"]
host = os.environ["DB_HOST_AWS"]
user = os.environ["DB_USER_AWS"]
port = os.environ["DB_PORT_AWS"]

# Constants
gas_price = 2.2087759717314484
electric_price = 0.103097091322717

def cost_to_own(car_price):
    
    ## Hard coded values - these are constants
    #car_price = 9999
    fuel_type = "gas"
    mpg = 25
    incentives = 0
    miles_per_year = 12000
    years = 5

    #Up front cost
    total_cost = car_price

    ## Annual cost
    if fuel_type == "gas":
        total_cost = car_price + (years * miles_per_year * gas_price / mpg)
        return total_cost
  
    else:
        return print("nice dude you have an electric car")



##Testing the cost to own function
#constants
#car_price = 9999
#print(cost_to_own(car_price))


def get_car_price(make, model, year):
    #This will be our sick machine learning model
    price = 30000 - ((2020 - year) * 2000 )

    return price

#Example JSON blob. This is the exact syntax we're getting from front end. 
data = {
    "make": "Geo",
    "model": "Metro",
    "year": 1992,
    "state": "HI",
    "fuel_type": "Gasoline",
    "mileage": 324230
}

make  = data["make"]
model = data["model"]
year = data["year"]
fuel_type = data["fuel_type"]
state = data["state"]
mileage = data["mileage"]


def getCO2_using_SQL(make, model, year):

    
    # Create connection to heroku database
    pg_conn = psycopg2.connect(dbname=name,
                           user=user,
                           password=password,
                           host=host,
                           port=port
                          )
    # Create cursor object
    pg_curs = pg_conn.cursor()

    # Test to see if its possible to make a query to the database
    pg_curs.execute(f"SELECT AVG(co2tailpipegpm) FROM epa_vehicles_all WHERE make = '{make}' AND model = '{model}' AND year = {year} ;")

    #SELECT AVG(co2tailpipegpm) FROM epa_vehicles_all WHERE make = ‘Ford’ AND model = ‘Probe’ AND year = ‘1994’


    tester = pg_curs.fetchall()[0]

    pg_curs.close()
    pg_conn.close()

    return tester


## We will need some error handling for mising values

def get_CO2_values(make, model, year):
    
    ### The average vehicle emits 4.6 metric tons/year
    ## This function is just a placeholder
    emissions = 4.6 + ((2020 - year) * .25 )


    return emissions


def get_electric_price(state):

    return round(electric_price*year, 2)

def get_gas_price(state):

    return round(gas_price*year, 2)



if __name__ == "__main__":


    print(f"Cost to own Function: {cost_to_own(9999)}")
    print(f"Get car price Function: {get_car_price(make, model, year, state, mileage)}")