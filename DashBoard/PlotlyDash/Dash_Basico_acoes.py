import yfinance as yf
import pandas as pd
#importando dash plotly
from dash import Dash, html, dash_table, dcc, Input, Output, callback
import plotly.express as px
import matplotlib.pyplot as plt
import dash_bootstrap_components as dbc
from dash.dash_table.Format import Format, Scheme, Sign

lista_de_simbolos = ['MSFT34.SA', 'PETR3.SA', 'AAPL34.SA']

#definindo Periodos
PERIODOS = ['5y','2y','1y','9mo','6mo','3mo','1mo','5d','2d']

df_global = pd.DataFrame()


#func para criar dataframe com todas as acoes nescessarias

def create_global_df(acoes:list, periodo:str='3mo' ):
    df_final = pd.DataFrame()
    dados = pd.DataFrame()
    for acao in acoes:
        dados = pd.DataFrame(yf.Ticker(acao).history(period=periodo)) #carrega o historico
        dados['Titulo'] = acao
        df_final = pd.concat([df_final,dados])
        
    return df_final.sort_values(by='Date')

@callback(
    Output(component_id='tabela-var-dia', component_property='data'),
    Input(component_id='escolha-de-acoes', component_property='value'),
)
def tabela_variacao(acoes_selecionadas):
    cont = 1
    df_ultima_var = pd.DataFrame(columns=['Titulo', 'Ultim.Var'])
    for acao in acoes_selecionadas:
        var_titulo = df_global[df_global['Titulo']==acao].sort_values(by='Date',ascending=False).head(2)['Close'].values.tolist()
        var = (var_titulo[0]-var_titulo[1])/var_titulo[1]
        df_ultima_var.loc[cont]=({'Titulo':acao, 'Ultim.Var':var})
        cont += 1
        
    return df_ultima_var[['Titulo','Ultim.Var']].to_dict('records')

#desenhando desenvolvimento acao
def grafico_principal(dados):
    fig = px.line(data_frame=dados,x=dados.index ,y=['Open'], color='Titulo')
    return fig

@callback(
    Output(component_id='carousel-items', component_property='items'),
    Input(component_id='escolha-de-acoes', component_property='value'),
)
def carousel_update(acoes_selecionadas):
    n_item = 0
    list_items_carousel = []
    for ticket in acoes_selecionadas:
        for item in yf.Ticker(ticket).news:
            n_item += 1
            try:
                header = item['title']
                href = item['link']
                src = item['thumbnail']['resolutions'][0]['url']
                list_items_carousel.append({ 'Key': str(n_item),'external_link':True, 'header':header, 'href':href, 'src':src })

            except :
                pass
    return list_items_carousel

#add controle
@callback(
    Output(component_id='grafico-01', component_property='figure'),
    Input(component_id='escolha-de-acoes', component_property='value'),
    Input(component_id='escolha-periodo-acoes', component_property='value')

)
def update_graph_01(acoes_selecionadas, periodo = '3mo'):
    df_global = create_global_df(acoes_selecionadas,periodo)
    #fintrando dados
    dados_filtrados = df_global.where(df_global['Titulo'].isin(list(acoes_selecionadas)))
    return grafico_principal(dados_filtrados)
    
@callback(
    Output(component_id='escolha-de-acoes', component_property='value'),
    Input(component_id='escolha-de-acoes', component_property='value')
)
def teste(acoes_selecionadas):
    if not len(acoes_selecionadas):
        return lista_de_simbolos[:1]
    return acoes_selecionadas
   


df_global = create_global_df(lista_de_simbolos)
df_variacao_acoes = tabela_variacao(lista_de_simbolos)
list_items_carousel = carousel_update(lista_de_simbolos)



#inicializar app

# Initialize the app - incorporate a Dash Bootstrap theme
external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets)

#definindo layout app
app.layout = dbc.Container([
    dbc.Row([
    html.H1('Acompanhamento de Ações' ,style={'backgroundColor':'white','text-align': 'center'} ),
    ]),

    dbc.Row([
        dbc.Col([
            html.Div('Escolha a ação:',style={'backgroundColor':'white'}),
            dcc.Dropdown(id='escolha-de-acoes',placeholder="Escolha uma Ação", options=lista_de_simbolos, multi=True, value=lista_de_simbolos),

            
        ],width=10),
        dbc.Col([
            html.Div('Escolha Periodo:',style={'backgroundColor':'white'}),
            dcc.Dropdown(id='escolha-periodo-acoes',placeholder="Escolha uma Periodo", options=PERIODOS, value='3mo'),

            
        ],width=2)
    
    ]),

    dbc.Row([
    dcc.Graph(figure={}, id='grafico-01')
    ]),

    dbc.Row([
        dbc.Col(
            [
            html.Div('News:',style={'backgroundColor':'white','text-align': 'center'}),
            dbc.Carousel(id='carousel-items' , interval=1000,
            items=list_items_carousel,
            className="carousel-fade", style={'backgroundColor':'white','vertical-align': 'middle'}
            )
        ],
          width=6),

        dbc.Col([
            dash_table.DataTable(id='tabela-var-dia',
                                 data=df_variacao_acoes, 
                                 page_size=10, 
                                 style_table={'overflowX': 'auto'},
                                 editable=True,
                                 style_cell={'textAlign': 'center'},
                                 style_data_conditional=[
                                     {
                                        'if':{'filter_query': '{Ultim.Var} < 0',
                                              'column_id': 'Ultim.Var',
                                            
                                              },
                                        'backgroundColor': '#85144b',
                                        'color': 'white'

                                     }
                                 ],
                                 columns = [
                                    dict(id='Titulo', name='Titulo'),
                                    dict(id='Ultim.Var', name='Ultim.Var', type='numeric',format=Format(scheme=Scheme.percentage, precision=2)),
                                            ]
                                 )
        ], width=6),
    ]),

])



if __name__ == '__main__':
    app.run(debug=True)
