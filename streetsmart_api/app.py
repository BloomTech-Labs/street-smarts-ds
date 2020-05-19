from flask import Flask, request, jsonify
from .modules import *
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

#Load credentials from .env
name = os.environ["DB_NAME_AWS"]
password = os.environ["DB_PW_AWS"]
host = os.environ["DB_HOST_AWS"]
user = os.environ["DB_USER_AWS"]


# Make app factory
def api():
    app = Flask(__name__)
    #app.config.from_object("config.Config")

    @app.route("/")
    def home():
        return "Streetsmart dummy endpoint"

    # This is our RC 1, this will always be up
    @app.route("/dummy", methods=['POST'])
    def dummy():
        req_data = request.get_json()

        samp = req_data["dummy"]

        output = {"success":samp}

        return output

    #This is predicting 
    @app.route("/pred", methods=['POST'])
    def summary():
        data = request.get_json()

        make  = data["make"]
        model = data["model"]
        year = data["year"]
        state = data["state"]
        fuel_type = data["fuel_type"]
        #odometer reading
        mileage = data["mileage"]

        
        #This is the prediction for the price of the vehicle
        price = get_car_price(make, model, year, state, mileage)
        #price = 9999
        
        # This is the five (x) year cost to own
        return jsonify({
            "cost_to_own":round(cost_to_own(price),2),
            "predicted_price":price,
            "predicted_CO2_emissions": get_CO2_values(make, model, year, fuel_type),
            "predicted_kWh": get_electric_price(state),
            "predicted_gas_cost": get_gas_price(state)
        })
    ## Endpoint 1: carbon emissions of vehicle
    # @app.route("/carbon_emissions", methods=['POST'])
    # def carbon():
    #     data = request.get_json()

    #     make  = data["make"]
    #     model = data["model"]
    #     year = data["year"]

    #     output = get_CO2_values(make, model, year)

    #     return jsonify({
    #     "predicted_CO2_emissions": output
    #     })


    ##endpoint 2: cost of vehicle
    @app.route("/price", methods=['POST'])
    def price():
        data = request.get_json()

        make  = data["make"]
        model = data["model"]
        year = data["year"]

        output = get_car_price(make, model, year)

        return jsonify({
        "predicted_price": output
        })

    @app.route("/tester", methods=["GET"])
    def test_aws():
        aws_test = test()
        return {"aws_test": aws_test}

    @app.route("/carbon_emissions", methods=["POST"])
    def test_aws2():

        data = request.get_json()

        make  = data["make"]
        model = data["model"]
        year = data["year"]


        aws_test = getCO2_using_SQL(make=make, model=model, year=year)
        return jsonify({"co2_tailpipe": aws_test})


    @app.route("/aws_test", methods=["POST"])    
    def test_aws_3():
        # Create connection to heroku database
        pg_conn = psycopg2.connect(dbname=name,
                            user=user,
                            password=password,
                            host=host
                            )
        # Create cursor object
        pg_curs = pg_conn.cursor()

        # Test to see if its possible to make a query to the database
        pg_curs.execute(f"SELECT AVG(co2tailpipegpm) FROM epa_vehicles_all WHERE make = '{make}' AND model = '{model}' AND year = {year} ;")

        #SELECT AVG(co2tailpipegpm) FROM epa_vehicles_all WHERE make = ‘Ford’ AND model = ‘Probe’ AND year = ‘1994’


        tester = pg_curs.fetchall()[0]

        pg_curs.close()
        pg_conn.close()
        return jsonify({"this is a test":tester})


    return app  