import os


SECRET_KEY = os.getenv('SECRET_KEY', 'replace with generated key here')

# SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"

# SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@localhost/exp1"
# SQLALCHEMY_DATAI = os.getenv('SQLALCHEMY_DATABASE_URI', "sqlite:///project.db")

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///project.db")


# postgres://postgresu1:isF6bNDtdYuZjEPNk0hOeIHn4U0vyNJk@dpg-cpk3c7f109ks73evcpp0-a.frankfurt-postgres.render.com/postdb1_yukk

# Inter postgresql://postgresu1:isF6bNDtdYuZjEPNk0hOeIHn4U0vyNJk@dpg-cpk3c7f109ks73evcpp0-a/postdb1_yukk
RESOURCE_SMOOTHIES = "resources/smoothies.csv"
RESOURCE_BENEFITS = "resources/benefits.csv"

