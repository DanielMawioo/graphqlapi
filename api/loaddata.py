import sqlite3
import pandas as pd

conn = sqlite3.connect('/home/vinny/projects/graphqlapi/db.sqlite3')
df = pd.read_csv('/home/vinny/projects/graphqlapi/dan.csv')
df['id']=df.index
df=df[['id', 'Segment', 'Country', 'Product', 'Units', 'Sales', 'Datesold']]
df.to_sql('api_productmodel', conn, if_exists='replace', index=False)