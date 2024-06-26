from classes.DBFetch import DBFetch
from classes.APIService import APIService
from queries.purchase_orders import purchase_orders
import pandas as pd


api = APIService()


def getAllPurchaseOrders():
    purchase_orders_id = DBFetch(purchase_orders).run()
    dfs_list = [getPurchaseOrderDetails(id) for id in purchase_orders_id.values.flatten()]
    df = pd.concat(dfs_list, ignore_index=True)
    df['created_at'] = pd.to_datetime(df['created_at'])

    return df


def getPurchaseOrderDetails(purchase_order_id):
    purchaseOrderData = api.getPurchaseOrderData(purchase_order_id)
    reduced_data = []
    order_number = purchaseOrderData["Codigo"]
    created_at = purchaseOrderData["DataEmissao"]
    company_id = purchaseOrderData["IdentificadorEmpresa"]

    try:
        for idx, item in enumerate(purchaseOrderData["Itens"]):
            for idx2, entry in enumerate(purchaseOrderData["Itens"][idx]["LancamentosCentroCusto"]):
                cost_centre_id = purchaseOrderData["Itens"][idx]["LancamentosCentroCusto"][idx2]["IdentificadorCentroDeCusto"]
                product_id = purchaseOrderData["Itens"][idx]["LancamentosCentroCusto"][idx2]["Identificador"]
                unit_cost = purchaseOrderData["Itens"][idx]["ValorUnitario"]
                order_qty = purchaseOrderData["Itens"][idx]["QuantidadePedida"]
                total_cost = purchaseOrderData["Itens"][idx]["ValorItem"]
                entry_value = purchaseOrderData["Itens"][idx]["LancamentosCentroCusto"][idx2]["ValorLancamento"]

                reduced_data.append({
                    'order_number' : order_number,
                    'created_at' : created_at,
                    'company_id' : company_id,
                    'cost_centre_id' : cost_centre_id,
                    'product_id' : product_id,
                    'unit_cost' : unit_cost,
                    'order_qty' : order_qty,
                    'total_cost' : total_cost,
                    'entry_value' : entry_value,
                })
        df = pd.DataFrame(reduced_data)

        return df
    
    except:
        raise Exception("Error while fetching data.")