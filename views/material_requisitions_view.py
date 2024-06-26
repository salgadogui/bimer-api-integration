from dash import html, dcc, Output, Input
import plotly.express as px
import modules.production as production
from app import app
import dash_ag_grid as dag
from components import dropdown


def material_requisitions_view():
    df = production.getMaterialRequisitions()

    return html.Div([
        html.Div([
            html.H2("Filtros"),
            dropdown.new('dropdown-filter', df['CdChamadaCC']),
            dropdown.new('dropdown-filter-2', df['StRequisicaoMaterialItem']),
            dropdown.new('dropdown-filter-3', df['CdChamadaInsumo'])
        ], style={'display': 'flex', 'flexDirection': 'row', 'gap': '30px'}),
        html.Div([
            html.Div([
                dcc.Loading(
                    id='loading-1',
                    type='circle',
                    children=dcc.Graph(figure={}, id='pie-graph', style={'width': '400px'}),
                ),
                dcc.Loading(
                    id='loading-2',
                    type='circle',
                    children=dcc.Graph(figure={}, id='hist-graph', style={'height': '450px'})
                )
            ], style={'display': 'flex', 'width':'100%'})
        ], style={'display': 'flex', 'flexDirection': 'column'},
        ),
        html.Div([
            dcc.Loading(
                id='loading-3',
                type='circle',
                children=dag.AgGrid(
                    id='table',
                    columnDefs=[{"headerName": col, "field": col} for col in df.columns],
                    rowData=df.to_dict('records'),
                )
            )
        ])
    ], style={'display': 'flex', 'flexDirection': 'column', 'gap': '30px'})

@app.callback(
    [Output(component_id='pie-graph', component_property='figure'),
     Output(component_id='hist-graph', component_property='figure'),
     Output(component_id='table', component_property='rowData')],
    [Input(component_id='dropdown-filter', component_property='value'),
     Input(component_id='dropdown-filter-2', component_property='value'),
     Input(component_id='dropdown-filter-3', component_property='value')]
)
def update_graph(filter_value, filter_value_2, filter_value_3):
    df = production.getMaterialRequisitions()
    filtered_df = df.copy()

    if filter_value:
        filtered_df = df[df['CdChamadaCC'] == filter_value]
    if filter_value_2:
        filtered_df = df[df['StRequisicaoMaterialItem'] == filter_value_2]
    if filter_value_3:
        filtered_df = df[df['CdChamadaInsumo'] == filter_value_3]

    pie_fig = px.pie(filtered_df, values='QtRequerida', names='NmEntidadeOrigem')

    hist_fig = px.histogram(
        filtered_df,
        histfunc='count',
        x='DtRequisicaoMaterial',
        y='QtRequerida',
        color='StRequisicaoMaterialItem',
        text_auto=True)
    
    hist_fig.update_layout(bargap=0.2)
    hist_fig.update_layout(legend=dict(orientation='h', yanchor='top', y=1.1, xanchor='left', x=0))
    table_data = filtered_df.to_dict('records')

    return pie_fig, hist_fig, table_data

