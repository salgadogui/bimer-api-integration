import dash_ag_grid as dag
from dash import dcc

def new(id, df):
    dcc.Loading(
        id='loading-3',
        type='circle',
        children=dag.AgGrid(
            id=f'{id}',
            columnDefs=[{"headerName": col, "field": col} for col in df.columns],
            rowData=df.to_dict('records'),
        )
    )
