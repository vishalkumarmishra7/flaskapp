
import csv
from config import RESOURCE_SMOOTHIES
from models import Smoothies, db


def initialize_db():
    delete_all_smoothies()
    # delete_all_benefits()
    insert_all_smoothies(RESOURCE_SMOOTHIES)
    # insert_all_benefits(RESOURCE_BENEFITS)
    
def delete_all_smoothies():
    Smoothies.query.delete()
    db.session.commit()
    
def delete_all_benefits():
    # Benefits.query.delete()
    db.session.commit()
    
def insert_all_smoothies(csv_file):
    with open(csv_file, 'r' , encoding='utf-8', errors='replace') as f:
        
        reader = csv.DictReader(f)
        
        for row in reader:
            item = Smoothies(
                recid=row['recid'],
                recipename=row['recipename'],
                description=row['description'],
                rest=row['rest'],
                ingredients=row['ingredients'],
                image=row['image'])
            db.session.add(item)
            
    db.session.commit()
    
