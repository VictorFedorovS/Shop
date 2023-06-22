from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class Brand(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    phones = db.relationship("Phone", back_populates="brand")

    def __str__(self):
        return f"{self.name}"


class Color(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    phones = db.relationship("Phone", back_populates="color")

    def __str__(self):
        return f"{self.name}"
    
class Description(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phones = db.relationship("Phone", back_populates="description")

    def __str__(self):
        return f"{self.name}"

class Phone(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    brand_pk = db.Column(db.Integer, db.ForeignKey("brand.pk", name="Brand"))
    brand = db.relationship("Brand", back_populates="phones")
    color_pk = db.Column(db.Integer, db.ForeignKey("color.pk", name="Color"))
    color = db.relationship("Color", back_populates="phones")
    description_pk = db.Column(db.Integer, db.ForeignKey("description.pk", name="Description"))
    description = db.relationship("Description", back_populates="phones")

    def __str__(self):
        return f"{self.name}"