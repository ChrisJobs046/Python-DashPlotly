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

#print(df.vacuna_nombre.unique())

#inicializando aplicacion de python por el parametro name
app = dash.Dash(__name__)


app.layout = html.Div([

    html.Div([

        html.H1('Vacunados por covid'),
        html.Img(src='../assets/COVID-19-outbreak-timeline.gif')
    ], className = 'banner')
])

if __name__ == '__main__':
    app.run_server(
        debug=True #port=8080
        )