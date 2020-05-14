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


def get_car_price(make, model, year, state, mileage):
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


## We will need some error handling for mising values

def get_CO2_values(make, model, year, fuel_type):
    
    return 11


def get_electric_price(state):

    return round(electric_price*year, 2)

def get_gas_price(state):

    return round(gas_price*year, 2)



if __name__ == "__main__":


    print(f"Cost to own Function: {cost_to_own(9999)}")
    print(f"Get car price Function: {get_car_price(make, model, year, state, mileage)}")