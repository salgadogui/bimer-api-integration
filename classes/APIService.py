import requests
import os
from classes.APIAuth import APIAuth

class APIService(APIAuth):
    def __init__(self):
        super().__init__()
    
    @APIAuth.ensure_authenticated
    def getPurchaseOrderData(self, purchase_order_id):
        url = f"{self.api_base_url}/compras/pedidos/{purchase_order_id}"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"PO {purchase_order_id}: Request successful! 200 OK")
            data = response.json()
            purchaseOrderData = data["ListaObjetos"][0]
            return purchaseOrderData
        else:
            print(f"Failed for PO {purchase_order_id}.")
            raise Exception(f"Failed to fetch pedido data: {response.status_code}, {response.text}")