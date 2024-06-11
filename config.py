import os


SECRET_KEY = os.getenv('SECRET_KEY', 'replace with generated key here')

# SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"

# SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@localhost/exp1"
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', "sqlite:///project.db")

RESOURCE_SMOOTHIES = "resources/smoothies.csv"
RESOURCE_BENEFITS = "resources/benefits.csv"

