from classes.DBFetch import DBFetch
from queries.material_requisitions import material_requisitions
from queries.production_orders import production_orders


def getMaterialRequisitions():
    df = DBFetch(material_requisitions).run()

    return df

def getProductionOrders():
    df = DBFetch(production_orders).run()

    return df