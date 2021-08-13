from geofusion_api.db.store_models import StoresTable
from flask_restful import Resource, reqparse


class Store(Resource):
    def post(self):
        arguments = reqparse.RequestParser()
        arguments.add_argument("name", type=str)
        arguments.add_argument("city", type=str)
        arguments.add_argument("state", type=str)
        arguments.add_argument("latitude", type=float)
        arguments.add_argument("longitude", type=float)
        arguments.add_argument("revenue", type=float)
        data = arguments.parse_args()
        customer = StoresTable(**data)

        try:
            customer.create_store()
        except:
            return {"message": "An internal error has ocurred."}, 500

        return customer.json()
