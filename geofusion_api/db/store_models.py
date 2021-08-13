from geofusion_api.db import db


class StoresTable(db.Model):
    __tablename__ = "Stores"
    index = db.Column("index", db.Integer, primary_key=True)
    name = db.Column("Name", db.String)
    city = db.Column("City", db.String)
    state = db.Column("State", db.String)
    latitude = db.Column("Latitude", db.Float)
    longitude = db.Column("Longitude", db.Float)
    revenue = db.Column("Revenue", db.Float)

    def __repr__(self, name):
        self.name = name

    def json(self):
        return {
            "index": self.index,
            "name": self.name,
            "city": self.city,
            "state": self.state,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "revenue": self.revenue,
        }

    def create_store(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_store(cls, index):
        store = cls.query.filter_by(index=index).first()
        if store:
            return store
        return None
