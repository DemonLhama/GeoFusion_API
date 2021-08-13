from flask_restful import Api
from flask import Blueprint
from geofusion_api.api.customers_resources import Customer, Customerstore
from geofusion_api.api.store_resources import Store
from geofusion_api.api.associates_resources import Associate
from geofusion_api.api.income_resouces import TotalIncome

api_bp = Blueprint("api", __name__)
api = Api(api_bp)


api.add_resource(Customer, "/customers")
api.add_resource(Customerstore, "/customers/<int:index>")
api.add_resource(Store, "/stores")
api.add_resource(Associate, "/revenue/<string:name_store>")
api.add_resource(TotalIncome, "/totalincome")
