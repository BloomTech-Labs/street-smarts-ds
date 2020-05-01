# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predicts the price of a used car


            Street Smarts is a car price predicting app that that provides car price predictions.


            """
        ),
        dcc.Link(dbc.Button('Try It!', color='primary'), href='/predictions')
    ],
    md=4,
)


layout = dbc.Row([column1])