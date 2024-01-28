from mongoengine.fields import StringField, IntField, FloatField, DictField
from database import db

class Part(db.Document):
    serial_number = StringField(unique=True, required=True)
    name = StringField(required=True)
    description = StringField(required=True)
    category = StringField(required=True)
    quantity = IntField(required=True)
    price = FloatField(required=True)
    location = DictField(required=True)

    meta = {
        'collection': 'parts' 
    }

    def to_json(self):
        return {"serial_number": self.serial_number,
                "name": self.name,
                "description": self.description,
                "category": self.category,
                "quantity": self.quantity,
                "price": self.price,
                "location": self.location,
                }

class Category(db.Document):
    name = StringField(unique=True, required=True)
    parent_name = StringField()

    meta = {
        'collection': 'categories' 
    }
    def to_json(self):
        return {"name": self.name,
                "parent_name": self.parent_name}