# Run app by typing "uvicorn main:app --reload" in terminal
# --reload lets you hot reload your app after making changes

from fastapi import FastAPI, Depends
from modules import Pred, status_200_or_nan

app = FastAPI()

@app.get("/")
async def root():
    return {"Street": "Smarts",
            "Version": "Developer",
            "API": "/docs",
            "By": "Jon Nguyen#-Dang, Will Stauffer-Norris, Mikio Harman"}

@app.post("/predict")
async def test_class(pred: Pred = Depends(Pred)):

    return {"car_price_prediction": round(pred.get_car_pred(), 2),
            "fuel_cost": round(pred.get_fuel_cost(), 2),
            "maintenance_cost": pred.maint,
            "five_year_cost_to_own": round(pred.cto(), 2),
            "co2_five_year_kgs": round(pred.co2_num_years(), 2), 
            "number_of_trees_to_offset": round(pred.co2_offset(), 0),
            "list_of_imgs": pred.fetch_img()} 