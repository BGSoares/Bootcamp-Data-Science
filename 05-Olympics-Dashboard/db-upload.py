import pandas as pd
from sqlalchemy import Table
from sqlalchemy import inspect
from sqlalchemy import MetaData
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()

user = os.getenv['PG_PASSWORD']
password = os.getenv['PG_PASSWORD']
host = 'db-spiced-northwind.c14q8hlm6x2l.eu-central-1.rds.amazonaws.com'
port = '5432'
database = 'olympics'

uri = f'postgresql://{user}:{password}@{host}:{port}/{database}'
engine = create_engine(uri, echo=False)

def drop_table_if_exists(table_name):
    if inspect(engine).has_table(table_name):
        table = Table(table_name, MetaData(engine), autoload_with=engine)
        table.drop()

# reload tables from csv files
data_dir= './data/'
files = os.listdir(data_dir)
for file in files:
    full_path = data_dir + file
    table_name = file.split('.')[0]
    ext = file.split('.')[1]
    if ext == 'xlsx':
        print('from %s file -> to "%s" table' % (full_path, table_name))
        drop_table_if_exists(table_name)
        df = pd.read_excel(full_path, index_col=0)
        df.to_sql(table_name, engine)