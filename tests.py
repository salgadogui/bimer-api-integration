import modules.procurement as procurement
import modules.production as production
from classes.MigrationService import MigrationService
import db.schema


def main():
    # df = production.getMaterialRequisitions()
    
    df = procurement.getAllPurchaseOrders()
    MigrationService().migrateData(df, db.schema.purchase_orders)
    
    # df = production.getProductionOrders()
    # MigrationService().migrateData(df, db.schema.production_orders)


if __name__ == "__main__":
    main()