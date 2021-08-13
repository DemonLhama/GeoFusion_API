from flask_restful import Resource
from geofusion_api.db.store_models import StoresTable
from geofusion_api.db.customer_models import CustomersTable


class TotalIncome(Resource):
    def get(self):
        stores = [store.json() for store in StoresTable.query.all()]
        customers = [customer.json() for customer in CustomersTable.query.all()]
        revenues = [stores[i].get("revenue") for i in range(len(stores))]
        total_income = sum(revenues)
        medium_total_income = total_income / len(customers)
        return {"message": "The total medium income is {}.".format(medium_total_income)}
