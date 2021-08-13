from geofusion_api.db.associates_models import Associates


def store_revenue(name_store):
    store = Associates.query.filter_by(name_store=name_store).first()
    store_data = store.json()
    revenue = store_data.get("Revenue")
    return revenue


def numbers_of_custumers(name_store):
    store_data = Associates.query.filter_by(name_store=name_store).all()
    customers_total = len(store_data)
    return customers_total
