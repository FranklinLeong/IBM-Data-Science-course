# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()


# print(spacex_df[spacex_df['class'] == 1].groupby(['Launch Site']).size().reset_index(name='count'))
entered_site = 'VAFB SLC-4E'
filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
print(filtered_df)
#count percentage of success and failure for each site
filtered_success_rate = filtered_df.groupby(['class']).size().reset_index(name='count')
filtered_success_rate['count'] = filtered_success_rate['count'] / filtered_success_rate['count'].sum() * 100
print(filtered_success_rate)
