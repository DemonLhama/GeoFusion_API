from geofusion_api.methods.associate_methods import store_revenue, numbers_of_custumers
from flask_restful import Resource


class Associate(Resource):
    def get(self, name_store):
        revenue = store_revenue(name_store)
        total_customers = numbers_of_custumers(name_store)
        if total_customers != 0:
            medium_income = revenue / total_customers
            return {
                "message": "The medium income for {} is {}".format(
                    name_store, medium_income
                )
            }
        return {"Medium Income": "0"}
