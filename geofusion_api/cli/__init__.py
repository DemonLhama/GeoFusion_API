from geofusion_api.db import db
from geofusion_api.db.associates_models import Associates
from geofusion_api.db.customer_models import CustomersTable
from geofusion_api.db.store_models import StoresTable


def init_app(app):
    @app.cli.command()
    def create_db():
        db.create_all()
