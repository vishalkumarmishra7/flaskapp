#Flask-Sqlalchemy model class
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text, TIMESTAMP

db = SQLAlchemy()

# class Smoothies2(db.Model):
#     recid = db.Column(db.Integer, primary_key=True)
#     recipename = db.Column(db.Text, nullable=False)
#     description = db.Column(db.Text, nullable=False)
#     rest = db.Column(db.Text, nullable=False)
#     ingredients = db.Column(db.Text, nullable=False)
#     image = db.Column(db.Text, nullable=False)    

#     def __repr__(self) -> str:
#         return f"Smoothie(recid={self.recid}, recipename={self.recipename}, image={self.image})"

class Smoothies(db.Model):
    recid = db.Column(db.Integer, primary_key=True)
    recipename = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rest = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)   

    def __repr__(self) -> str:
        return f"Smoothie(recid={self.recid}, recipename={self.recipename}, image={self.image})"
 
