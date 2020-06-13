# first we need to import our sqlite3 from DB API 
#DB API IS interface for managing the diffrent databases mudules
import sqlite3
conn=sqlite3.connect('students')
# we need to declaring cursor to query row by row
cursor=conn.cursor()
query='''
select * 
from students
'''
#executing our query
cursor.execute(query)
rows=cursor.fetchall()
# rows is list of all our row result query table
for row in rows:
    print(f'the first name id {row[0]}')