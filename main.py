import pandas as pd
import numpy as np
import random
from faker import Faker
from sqlalchemy import create_engine
import pymysql

# Generate sample data using faker for fake names and info
fake = Faker()
data = {
    "customer_id": np.arange(1001, 1201),
    "customer_name": [fake.name() for _ in range(200)],
    "product_id": np.random.randint(1, 21, 200),
    "purchase_date": [fake.date_between(start_date='-1y', end_date='today') for _ in range(200)],
    "quantity": np.random.randint(1, 11, 200),
    "price_per_unit": np.round(np.random.uniform(10.0, 1000.0, 200), 2),
    "region": [random.choice(["North", "South", "East", "West"]) for _ in range(200)],
}
df = pd.DataFrame(data)

# Data connection to sql
db_connection_string = "mysql+pymysql://root:Manas0086@localhost/Cust_product"
engine = create_engine(db_connection_string)

# Insert Data into SQL
df.to_sql('purchases', con=engine, if_exists='append', index=False)


# retriving data from sql
query = "SELECT * FROM purchases"
with engine.connect() as connection:
    df = pd.read_sql(query, connection)
    print(df.head())
