from math import sqrt
from geofusion_api.db.store_models import StoresTable
from geofusion_api.db.customer_models import CustomersTable
from geofusion_api.db.associates_models import Associates
from flask_restful import Resource, reqparse


class Customer(Resource):
    def post(self):
        arguments = reqparse.RequestParser()
        arguments.add_argument("name", type=str)
        arguments.add_argument("city", type=str)
        arguments.add_argument("state", type=str)
        arguments.add_argument("latitude", type=float)
        arguments.add_argument("longitude", type=float)
        data = arguments.parse_args()
        customer = CustomersTable(**data)

        try:
            customer.create_customer()
        except:
            return {"message": "An internal error has ocurred."}, 500

        return customer.json()


class Customerstore(Resource):
    def get(self, index):
        customer = CustomersTable.find_customer(index)
        if customer:
            customer_data = customer.json()
            cust_lati = customer_data.get("latitude")
            cust_long = customer_data.get("longitude")
            stores = [store.json() for store in StoresTable.query.all()]
            store_lat = [stores[i].get("latitude") for i in range(len(stores))]
            store_long = [stores[i].get("longitude") for i in range(len(stores))]
            distance = []
            for store in range(len(stores)):
                distance_set = sqrt(
                    ((store_long[store] - cust_long) ** 2)
                    + ((store_lat[store] - cust_lati) ** 2)
                )
                distance.append(distance_set)
            closest_store = stores[distance.index(min(distance))]
            print(closest_store.get("revenue"))
            associate = Associates(
                name_customer=customer_data.get("name"),
                name_store=closest_store.get("name"),
                revenue=closest_store.get("revenue"),
            )
            try:
                associate.create_associate()
            except:
                return {"message": "An internal error has ocurred."}, 500
            return associate.json()
        return {"message": "Customer not found"}
