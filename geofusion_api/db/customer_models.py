from geofusion_api.db import db


class CustomersTable(db.Model):
    __tablename__ = "Customers"
    index = db.Column("index", db.Integer, primary_key=True)
    name = db.Column("name", db.String)
    city = db.Column("city", db.String)
    state = db.Column("state", db.String)
    latitude = db.Column("latitude", db.Float)
    longitude = db.Column("longitude", db.Float)

    def __repr__(self, index):
        self.index = index

    def json(self):
        return {
            "index": self.index,
            "name": self.name,
            "city": self.city,
            "state": self.state,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }

    def create_customer(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_customer(cls, index):
        customer = cls.query.filter_by(index=index).first()
        if customer:
            return customer
        return None
