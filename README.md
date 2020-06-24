

# Street Smarts #

You can find the project at [streetsmarts.online](www.streetsmarts.online).

![streetsmartsgif](https://raw.githubusercontent.com/willstauffernorris/willstauffernorris.github.io/master/img/streetsmartsgiphy.gif)   

## Contributors

| [Will Stauffer-Norris](https://github.com/willstauffernorris)                                                                                 | [Jon Nguyen](https://github.com/JonNData)                                                                                                                         | [Mikio Harman](https://github.com/mpHarm88)                                                                                                                       |
| :-------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------: |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [<img src="https://avatars3.githubusercontent.com/u/30095633?s=460&u=394f507349eee136ae1beec2112436b13de9609a&v=4" width = "200" />](https://github.com/willstauffernorris)   | [<img src="https://avatars2.githubusercontent.com/u/59704644?s=460&u=63f5db90b599e70770504e2b86047dd91dc441e2&v=4" width = "200" />](https://www.linkedin.com/in/jonathan-nguyen-94344b21/) | [<img src="https://avatars3.githubusercontent.com/u/49764112?s=460&u=8ab39b1438191f5f94f11f1fb042154c3e54716a&v=4" width = "200" />](https://github.com/mpHarm88) |
| [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/willstauffernorris)                                         | [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/JonNData)                                                                              | [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/mpHarm88)                                                                             |
| [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/willsn/) | [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/jonathan-nguyen-94344b21/)                                       | [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/mikio-harman-6342a9195/)                            |


![MIT](https://img.shields.io/packagist/l/doctrine/orm.svg)
![Python](https://img.shields.io/badge/python-v3.7-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-0.22-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-0.55.1-blue)
![FuzzyWuzzy](https://img.shields.io/badge/RapidFuzz-0.9.1-blueviolet)
![Pandas](https://img.shields.io/badge/Pandas-1.0.4-green)
![Heroku](https://img.shields.io/badge/Heroku-10-blueviolet)

More info on using badges [here](https://github.com/badges/shields)

## Project Overview


[Trello Board](https://trello.com/b/B5GkoOPo/labs-24-street-smarts)

[Product Canvas](https://www.notion.so/Street-Smarts-Automotive-Data-5450e77cf0c44a218a4aa6d67ce889eb)

Street Smarts helps you discover the value and carbon emissions of your car, and compare it to other cars.

We use deep learning in our state-of-the-art machine learning model to predict current prices.

Unlike the dealers, we also display the carbon emissions for your car, so you can make a responsible purchase.

[Deployed Front End](www.streetsmarts.online)

### Tech Stack

- [Python](https://www.python.org/)
- [Heroku](https://signup.heroku.com/t/platform?c=70130000001xDpdAAE&gclid=Cj0KCQjwiYL3BRDVARIsAF9E4GfSpj6ILAdSsgB8lle2cKVF_KAiQEfWAwEczYAHzpZtkf-nu9K7sgAaAgYVEALw_wcB)
- [SciKit Learn](https://scikit-learn.org/stable/)
- [Fast API](https://fastapi.tiangolo.com/)
- [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)
- [AWS Relational Databse Service](https://aws.amazon.com/rds/)

### Predictions
```javascript
# Input 

{
'make': 'Ford',
'model': 'F150 Pickup 4WD'
'year': 2005
}
```


```javascript
# Outputting Route

{
  "car_price_prediction": 30655.23,
  "fuel_cost": 16071.43,
  "maintenance_cost": 1000,
  "five_year_cost_to_own": 47726.66,
  "co2_five_year_kgs": 47608.93,
  "number_of_trees_to_offset": 437,
  "list_of_imgs": [
    "https://images.craigslist.org/00l0l_aZwW2Ok8T8T_600x450.jpg",
    "https://images.craigslist.org/00l0l_aZwW2Ok8T8T_600x450.jpg"
  ]
}
```

### Explanatory Variables

1. Model
	* This is the model of the vehicle.
2. Make
	* This is the make of the vehicle.
3. Year
	* The year of the vehicle.


### Data Sources

-   [EPA Fuel Economy dataset](https://www.fueleconomy.gov/feg/ws/index.shtml#vehicle)

-   [Craigslist Dataset](https://www.kaggle.com/austinreese/craigslist-carstrucks-data)


### Python Notebooks

[Official_大_Data_ 🧮_Cleaning_🧹_Notebook_📓](https://github.com/Lambda-School-Labs/street-smarts-ds/blob/master/notebooks/Official_%E5%A4%A7_Data_%20%F0%9F%A7%AE_Cleaning_%F0%9F%A7%B9_Notebook_%F0%9F%93%93.ipynb)

[SQL](https://github.com/Lambda-School-Labs/street-smarts-ds/blob/master/notebooks/sql.ipynb)

[Plotly Dash App Data Viz 📉](https://github.com/Lambda-School-Labs/street-smarts-ds/blob/master/notebooks/Plotly%20Dash%20App%20Data%20Viz%20%F0%9F%93%89.ipynb)

[streetsmart_EPA_vehicles_EDA](https://github.com/Lambda-School-Labs/street-smarts-ds/blob/master/notebooks/streetsmart_EPA_vehicles_EDA.ipynb)

[official_streetsmarts_pytest](https://github.com/Lambda-School-Labs/street-smarts-ds/blob/master/notebooks/official_streetsmarts_pytest.ipynb)


### How to connect to the data API


Our initial release canvases included a Flask API with dummy endpoints to Heroku, hosting a database on there as well.  
  
To access the version of the repo that was deployed to Heroku:  
clone the repo     
access our commit with:    
`git checkout 1ff857091d07a4e13455aeba0e7bc4b0137434be`  

https://streetsmartdummy.herokuapp.com/pred

Example Input:
```
{
	"make":"this is a test",
	"model": "ford",
	"year":1995,
	"fuel_type":"gas",
	"state":"CA",
	"mileage":100
}
```

Example Output:
```
{
    "cost_to_own": -14698.94,
    "predicted_CO2_emissions": 11,
    "predicted_gas_cost": 4399.88,
    "predicted_kWh": 205.37,
    "predicted_price": -20000
}
```

Our current FAST api is deployed on AWS with  easily accessed docs at:  

http://data.streetsmarts.online/docs

Input:
```{
miles_per_year: int = 15000,
num_years: int = 5,
gas_cost: int = 3,
electrical_cost: float = 0.12,
maintenance_cost_per_year: int = 1000,
make: str='Ford',
model: str='F150 Pickup 4WD',
year: int=2005,
odometer: int=99999
}
```

Output:  
```
{
  "car_price_prediction": 30655.23,
  "fuel_cost": 16071.43,
  "maintenance_cost": 1000,
  "five_year_cost_to_own": 47726.66,
  "co2_five_year_kgs": 47608.93,
  "number_of_trees_to_offset": 437,
  "trees_burned_emoji": [
    "🔥🔥🔥🔥🌲🌲🌲🌲🌲🌲"
  ],
  "list_of_imgs": [
    "https://images.craigslist.org/00E0E_av8sHn7jwty_600x450.jpg"
  ]
}
```

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a [code of conduct](./code_of_conduct.md.md). Please follow it in all your interactions with the project.

### Issue/Bug Request

 **If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**
 - Check first to see if your issue has already been reported.
 - Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
 - Create a live example of the problem.
 - Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes,  where you believe the issue is originating from, and any potential solutions you have considered.

### Feature Requests

We would love to hear from you about new features which would improve this app and further the aims of our project. Please provide as much detail and information as possible to show us why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this app, please submit a pull request. It is best to communicate your ideas with the developers first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

Remember that this project is licensed under the MIT license, and by submitting a pull request, you agree that your work will be, too.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to our existing code conventions and test coverage.
- Include the relevant issue number, if applicable.
- You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).

## Documentation

See [Backend Documentation](https://github.com/Lambda-School-Labs/street-smarts-be) for details on the backend of our project.

See [Front End Documentation](https://github.com/Lambda-School-Labs/street-smarts-fe) for details on the front end of our project.
