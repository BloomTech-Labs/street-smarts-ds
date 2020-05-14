from flask import Flask, request, jsonify
from .modules import cost_to_own, get_car_price, get_CO2_values, gas_price, electric_price, get_gas_price, get_electric_price

# Make app factory
def api():
    app = Flask(__name__)

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
     
    return app  