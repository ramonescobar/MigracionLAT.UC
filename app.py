#Importando paquetes necesarios
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import colores
import plotly.figure_factory as ff

lista =['Antigua y Barbuda','Argentina','Bahamas','Barbados','Belice',
        'Bolivia','Brasil','Chile','Colombia','Costa Rica','Cuba',
        'República Dominicana','Ecuador','El Salvador','Granada',
        'Guatemala','Guyana','Haiti','Honduras','Jamaica','México',
        'Nicaragua','Panama','Paraguay','Perú','San Cristóbal y Nieves',
        'Santa Lucía','San Vicente y las Granadinas','Surinam', 'Trinidad y Tobago',
        'Uruguay','Venezuela']

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
#server=app.server
#Importando bases de datos
df=pd.read_csv('MXP.csv', sep=";")
df2 =pd.read_csv("Net_Migration.csv", sep=';')
df3=pd.read_csv('1022be19-c0ef-473b-9c38-f5de90877db0_Data.csv', sep=';')

#App
app=dash.Dash(__name__)

Cols=list(df2)
Cols2=list(df3)

app.layout=html.Div(
    className='principal',
    children=[
    html.Div(
        className='title',
        children=[
            html.Div(className='imagenUC',children=[html.Img(src='/assets/logo-uc-size-02.PNG')]),
            html.Div(
                className='titulo_principal',
                children=[html.H1("Migración en Latinoamérica")]),
                html.Br()]),
    html.Div(
        className='mapa-g',
        children=[
            html.Br(),
            html.H3("Seleccione el país de llegada:",
                style={'width':'50%'}),
            dcc.Dropdown(
                id='Drop-Countries',
                style={'width': '50%', 'display':'inline-block'},
                options=[{"label":i,"value":i} for i in lista],
                value='Chile'),
            dcc.Graph(
                id="Map-mig",
                animate=True,
                style={'backgroundColor': colors['background']}
                )],
                style={'width':'48%','height':'50%', 'display':'inline-block'}
            ),
    html.Div(
        className='barmig',
        children=[
            html.Br(),
            dcc.Graph(
                id='Bar-mig-country',
                #style={'width': '48%', 'align':'center'})]),
                 )],
                style={'width':'48%','height':'50%', 'display':'inline-block'}
            ),
    html.Br(),
    html.H1("Comparación de perfiles por país (De Entrada y Salida)",className='titulo-perfiles'),
    html.Div(
        className='profile1',
        children=[
            html.H3('Selecciones un país de entrada:',style={"display":"inline-block"}),
            html.Div(
                className='drop-cperfil1',
                children=[
                    dcc.Dropdown(
                            id='dp1',
                            options=[{'label':i, 'value':i} for i in df3['Country Name'].unique()],
                            value='Chile')]),
            html.Br(),
            html.Div(
                className='Pro1',
                children=[
                    dcc.Graph(
                        id='Perfil1')])
            ]),
    html.Div(
        className='profile2',
        children=[
            html.H3('Selecciones un país de salida:',style={"display":"inline-block"}),
            html.Div(
                className='drop-cperfil2',
                children=[
                    dcc.Dropdown(
                        id='dp2',
                        options=[{'label':i, 'value':i} for i in df3['Country Name'].unique()],
                        value='El Salvador')]),
        html.Br(),
        html.Div(
            className='pro2',
            children=[
                dcc.Graph(
                    id='Perfil2')])]),
    html.Br(),
    html.Div(
        className='graph-bar-netmigration',
        children=[
            html.Br(),
            html.Div(
                className='Radio-years',
                children=[
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.H3("Año de análisis:"),
                    dcc.RadioItems(
                        id="Drop_years",
                        options=[{"label":Cols[i],"value":Cols[i]} for i in range(4, len(Cols))],
                        value="2017 [YR2017]"),
                    html.Br(),
                    html.Br(),
                    html.Br()
                    ]),
        html.Div(
            className='barras-nm',
            children=[
                dcc.Graph(
                    id="Net-mig")])
    ]),
    html.Div(
        className='footer',
        children=[
            html.Div(
                className='Bibliografias',
                children=[
dcc.Markdown(
'''
### Fuentes
#### [Indicadores del Banco Mundial](https://data.worldbank.org/indicator)
#### [Revista Expansión](http://www.expansion.com/)
'''
)
                ]
            ),
            html.Div(
                className='info',
                children=[
                dcc.Markdown('''
## Disponible en:
### [Github](https://github.com/calvarad/p-g1)
                    ''')
                ]
            ),
            html.Div(
                className='creadores',
                children=[
                dcc.Markdown('''
## Desarrollado por:
### David Cornejo [(drcornejo@uc.cl)](mailto:drcornejo@uc.cl)
### Ramón Escobar [(rlescobar@uc.cl)](mailto:rlescobar@uc.cl)
### Gabriela Reyes [(ggreyes@uc.cl)](mailto:ggreyes@uc.cl)
                ''')
                ]
            )
        ]
    )
])


#Funciones para int
@app.callback(
    Output('Map-mig', 'figure'),
    [Input('Drop-Countries', 'value')])

def callback_map(country):
    dff = df[df["País de entrada"] == country]
    fig = {
        'data': [go.Choropleth(
            locations = dff['iso3'],
            z = dff['Número de personas'],
            text = dff['Países de salida'],
            colorscale = colores.escala,
        )],
        'layout':{
            'title':"Inmigrantes en {} según país de origen (2017)".format(country),
            'geo':dict(
                center = dict(lon = -60, lat = -15),
                projection = dict(scale = 2))},
            }
    return fig

@app.callback(
    Output('Net-mig', 'figure'),
    [Input('Drop_years', 'value')])
def callback_graph(selection_y):
    dg=df2[df2["Series Code"]=="SM.POP.NETM"].sort_values(by=selection_y, ascending=True)
    fig2 = {
        'data': [
            go.Bar(
                x =dg["Country Name"],
                y = dg[selection_y],
                text=dg["Country Code"],
                textposition = "inside",
                textfont={
                    'color':'rgb(255, 255, 255)'
                })],
        'layout': go.Layout(
            title = "Migración neta en {} ".format(selection_y),
            yaxis = {'title':"Migración neta por país"},
            margin = {
                'l':100,
                'b':125},
            height = 500
        )
    }
    return fig2

@app.callback(
    Output('Bar-mig-country', 'figure'),
    [Input('Drop-Countries', 'value')])

def callback_graph_country_bar(pais_ingreso):
    dt=df[df["País de entrada"] == pais_ingreso].sort_values(by='Número de personas', ascending=True)
    fig3 = {
        'data':[
            go.Bar(
                x=dt['iso3'],
                y=dt['Número de personas'],
                text=dt['Países de salida']
            )
        ],
        'layout':
            go.Layout(
                title='Migrantes en total viviendo en {} (2017)'.format(pais_ingreso),
                xaxis = {'title':"Paises de América Latina"},
                yaxis = {'title':"Migración neta por país"},
                margin = {'l':100,
                         'b':125},
                height = 500
            )
    }
    return fig3

@app.callback(
    Output('Perfil1', 'figure'),
    [Input('dp1', 'value')])
def gen_table_1(countryp1):
    dfp1=df3[df3['Country Name']==countryp1]
    ind1=['Indicador']
    val1=['Valor']
    figt1=ff.create_table(
        dfp1[['Series Name','2016 [YR2016]']],
        height_constant=25,
        colorscale=colores.escala_tabla)
    return figt1

@app.callback(
    Output('Perfil2', 'figure'),
    [Input('dp2', 'value')])
def gen_table_2(countryp2):
    dfp2=df3[df3['Country Name']==countryp2]
    ind2=['Indicador']
    val2=['Valor']
    figt2=ff.create_table(
        dfp2[['Series Name','2016 [YR2016]']],
        height_constant=25,
        colorscale=colores.escala_tabla)
    return figt2

if __name__ == '__main__':
    app.run_server()
