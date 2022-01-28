from sqlalchemy import text, create_engine
import os
from dotenv import load_dotenv
load_dotenv()

USERNAME = os.getenv('PG_USER')
PASSWORD = os.getenv('PG_PASSWORD')
HOST = 'localhost' # you can use your RDS instance here as well
PORT = '5432'
DB = 'northwind'

conn_string = f'postgresql://{HOST}:{PORT}/{DB}'
engine = create_engine(conn_string)

try:
    query = '''
    ALTER TABLE order_details
    orderid NOT NULL
    productid NOT NULL
    ADD CONSTRAINT order_details_pk
    PRIMARY KEY (orderid, productid);
    '''
    engine.execute(query)
except:
    pass


try:
    query = '''
    ALTER TABLE categories
    ADD CONSTRAINT categories_pk
    PRIMARY KEY (categoryid);
    '''
    engine.execute(query)
except:
    pass


try:
    query = '''
    ALTER TABLE customers
    ADD CONSTRAINT customers_pk
    PRIMARY KEY (customerid);
    '''
    engine.execute(query)
except:
    pass


try:
    query = '''
    ALTER TABLE employee_territories
    ADD CONSTRAINT employee_territories_pk
    PRIMARY KEY (employeeid);
    '''
    engine.execute(query)
except:
    pass


try:
    query = '''
    ALTER TABLE employees
    ADD CONSTRAINT employees_pk
    PRIMARY KEY (employeeid);
    '''
    engine.execute(query)
except:
    pass


try:
    query = '''
    ALTER TABLE orders
    ADD COSNTRAINT orders_pk
    PRIMARY KEY (orderid);
    '''
    engine.execute(query)
except:
    pass


try:
    query = '''
    ALTER TABLE products
    ADD CONSTRAINT products_pk
    PRIMARY KEY (productid);
    '''
    engine.execute(query)
except:
    pass


try:
    query = '''
    
    '''
    engine.execute(query)
except:
    pass







try:
    query = '''
    
    '''
    engine.execute(query)
except:
    pass