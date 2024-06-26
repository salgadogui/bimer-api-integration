purchase_orders = \
    """
    SELECT
        IdPedidoDeCompra
    FROM
        PedidoDeCompra
    ORDER BY
        DtEmissao DESC
    """
