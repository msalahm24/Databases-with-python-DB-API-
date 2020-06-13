# first we need to import our sqlite3 from DB API 
#DB API IS interface for managing the diffrent databases mudules
import sqlite3
def select(query,db):
    conn=sqlite3.connect(db)
    # we need to declaring cursor to query row by row
    cursor=conn.cursor()
    query=query
    #executing our query
    try:
        cursor.execute(query)
        rows=cursor.fetchall()
    except DatabaseError:
        print('check your database connection')
    finally:
        conn.close()
    # rows is list of all our row result query table
    return rows
def insertnewrow(query,db):
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    query=query
    try:
        cursor.except(query)
        # Atomicity :- the transaction happens as a whole or not at all
        conn.commit()
    except DatabaseError:
        print('check your connection')
    finally:
        conn.close()
