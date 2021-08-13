from geofusion_api.db import db


class Associates(db.Model):
    __tablename__ = "Associates"
    index = db.Column("index", db.Integer, primary_key=True)
    name_customer = db.Column("Customer", db.String)
    name_store = db.Column("Store", db.String)
    revenue = db.Column("Revenue", db.ForeignKey("Stores.Revenue"))

    def __repr__(self, name_customer, name_store, revenue):
        self.name_customer = name_customer
        self.name_store = name_store
        self.revenue = revenue

    def json(self):
        return {
            "index": self.index,
            "Customer": self.name_customer,
            "Store": self.name_store,
            "Revenue": self.revenue,
        }

    def create_associate(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def search_store(cls, name_store):
        store = cls.query.filter_by(name_store=name_store).all()
        return store
