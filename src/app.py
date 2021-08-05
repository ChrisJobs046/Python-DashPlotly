import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

#df es un dataframe
df = pd.read_csv('../assets/Covid19VacunasAgrupadas.csv')

#print(df)

#print(df.vacuna_nombre.nunique())

print(df.vacuna_nombre.unique())

