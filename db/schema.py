from sqlalchemy import MetaData, Table, Column, Integer, String, Numeric

metadata = MetaData()

purchase_orders = Table(
    'purchase_orders', metadata,
    Column('order_number', Integer, primary_key=True),
    Column('company_id', String),
    Column('cost_centre_id', String),
    Column('product_id', String),
    Column('unit_cost', Numeric(precision=8, scale=2)),
    Column('order_qty', Numeric(precision=2, scale=2)),
    Column('total_cost', Numeric(precision=8, scale=2)),
    Column('entry_value', Numeric(precision=8, scale=2)),
    Column('created_at', String)
)

production_orders = Table(
    'production_orders', metadata,
    Column('order_number', Integer, primary_key=True),
    Column('nm_empresa', String),
    Column('cd_chamada', String),
    Column('nm_produto', String),
    Column('qt_os_emitidas', Integer),
    Column('qt_pedida_pv', Integer),
    Column('qt_atendida_pv', Integer),
    Column('qt_restante_pv', Integer),
    Column('percentual_concluido_pv', Numeric(precision=5, scale=2)),
    Column('cd_os_emitidas', String),
    Column('dt_limite_servico', String)
)
