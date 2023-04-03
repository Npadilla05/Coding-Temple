from dotenv import load_dotenv
from os import getenv
import psycopg2
import pandas as pd
from sqlalchemy.types import Integer, Text, String, Float

# databaselanguage(postgresql)://user:password@url:port/database_name
connection = 'postgresql://tmjtybmx:WPoIaEgtoD8B9wpRRlVPG2zheO4bcdkY@lallah.db.elephantsql.com/tmjtybmx'

titanic = pd.read_csv(r'C:\Users\Noki\week_5\titanic.csv')

[print(v) for v in titanic if v == '']
# .to_sql() writes your dataframe object to a database, you specify the schema, or structure of the database
titanic.to_sql('titanic',
               index=False,
               con=connection,
               if_exists='replace',
               dtype={
               'Survived': Integer,
               'Pclass': Integer,
               'Name': String,
               'Sex': String,
               'Age': Float,
               'Siblings/Spouses_Aboard': Integer,
               'Parents/Children_Aboard': Integer,
               'Fare': Float
               })
               
            