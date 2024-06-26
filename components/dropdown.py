from dash import dcc


def new(id, df):
    Dropdown = dcc.Dropdown(
        id=f'{id}',
        options=[{'label': val, 'value': val} for val in sorted(df.drop_duplicates().unique(), reverse=True)],
        value=None,
        multi=False,
        placeholder=f'Selecione {df.name}',
        style={'width':'300px'}
    )    

    return Dropdown
