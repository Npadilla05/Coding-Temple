import requests
import pandas as pd
from dotenv import load_dotenv
import pymongo
import os

dfmath = pd.read_csv(r'C:\Users\Noki\AppData\Local\Temp\Rar$DIa1532.12227\student-mat.csv', sep=';')
dfpor = pd.read_csv(r'C:\Users\Noki\AppData\Local\Temp\Rar$DIa1532.12669\student-por.csv', sep= ';')

dfmath.columns = dfmath.columns.str.lower()
dfpor.columns = dfpor.columns.str.lower()

dfmath.rename(columns={'g1': 'math_g1', 'g2': 'math_g2', 'g3': 'math_g3'}, inplace=True)
print(dfmath.columns)
dfpor.rename(columns={'g1': 'por_g1', 'g2': 'por_g2', 'g3': 'por_g3'}, inplace=True)
print(dfpor.columns)

new_df = pd.concat([dfpor,dfmath],ignore_index=True)

new_df = new_df.drop_duplicates()

duplicates = new_df.duplicated()
print("Number of duplicate records: ", duplicates.sum())

load_dotenv()
mongo_url = os.getenv('MONGO_URL')
client = pymongo.MongoClient(mongo_url)

db = client.db
student_perf = db.student_perf

for i in new_df.index:
    student_perf.insert_one(new_df.loc[i].to_dict())