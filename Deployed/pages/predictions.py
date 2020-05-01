# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import jsonify
from flask import request

# Imports from this application
from app import app

from joblib import load
pipeline = load('assets/pipeline.joblib')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Year'), 
        dcc.Input(
            id='Year', 
            placeholder='Enter Vehicle Year',
            type='number',
            value=0, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Mileage'), 
        dcc.Input(
            id='Mileage', 
            placeholder='Enter Mileage',
            type='number',
            value=0, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### City'), 
        dcc.Input(
            id='City', 
            placeholder='Enter City',
            type='text',
            value='', 
            className='mb-5', 
        ),
        dcc.Markdown('#### State'), 
        dcc.Input(
            id='State', 
            placeholder='Enter State',
            type='text',
            value='', 
            className='mb-5', 
        ),
        dcc.Markdown('#### VIN'), 
        dcc.Input(
            id='Vin', 
            placeholder='Enter VIN',
            type='text',
            value='', 
            className='mb-5', 
        ),
        dcc.Markdown('#### Make'), 
        dcc.Input(
            id='Make', 
            placeholder='Enter Make',
            type='text',
            value='', 
            className='mb-5', 
        ),
        dcc.Markdown('#### Model'), 
        dcc.Input(
            id='Model', 
            placeholder='Enter Model',
            type='text',
            value='', 
            className='mb-5', 
        ),
    ],
    md=4,
)

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# app.layout = html.Div([
#     html.Div(dcc.Input(id='input-box', type='text')),
#     html.Button('Submit', id='button'),
#     html.Div(id='output-container-button',
#              children='Enter a value and press submit')
# ])


column2 = dbc.Col(
    [
        html.H2('Expected Price', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2])

import pandas as pd


@app.callback(
    Output('prediction-content', 'children'),
    [Input('Year', 'value'), Input('Mileage', 'value'), Input('City', 'value'), Input('State', 'value'), Input('Vin', 'value'), Input('Make', 'value'), Input('Model', 'value')],
)
# @app.callback(
#     dash.dependencies.Output('output-container-button', 'children'),
#     [dash.dependencies.Input('button', 'n_clicks')],
#     [dash.dependencies.State('input-box', 'value')])
# def update_output(n_clicks, value):
#     return 'The input value was "{}" and the button has been clicked {} times'.format(
#         value,
#         n_clicks
#     )


# if __name__ == '__main__':
#     app.run_server(debug=True)

def predict(Year, Mileage, City, State, Vin, Make, Model):
    # test = {"Year": [2015],
    #         "Mileage": [30000],
    #         "City": ["Louisville"],
    #         "State": ["KY"],
    #         "Vin": ["FA6P8CF7F5348710"],
    #         "Make": ["Ford"],
    #         "Model": ["MustangFastback"]
    #         }
    df = pd.DataFrame(
         columns=['Year', 'Mileage', 'City', 'State', 'Vin', 'Make', 'Model'], 
         data=[[float(Year), float(Mileage), City, State, Vin, Make, Model]]
    )
    y_pred = pipeline.predict(df)[0]
#    return df
    return f'${y_pred:.0f}'