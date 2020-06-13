# "Database code" for the DB Forum.

import datetime
import psycopg2



POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():

  try:
    global conn
    conn=psycopg2.connect(user='postgres', password='12369478521',host='127.0.0.1',port='5432', database='forum')
    cursor=conn.cursor()
    print('ok')
    query='''
    select content,time
    from posts
    order by time desc 
    '''
    cursor.execute(query)
    POSTS=cursor.fetchall()
  except(Exception,psycopg2.Error) as error:
    print(f'your error is {error}')
  finally:
    if (conn):
       conn.close()
        
  return POSTS

def add_post(content):
  try:
    global conn
    conn=psycopg2.connect(user='postgres', password='12369478521',host='127.0.0.1',port='5432',database='forum')
    cursor=conn.cursor()
    print('ok')
    # to prevent sql injection
    cursor.execute("insert into posts values(%s)" ,(content,))
    conn.commit()
  except(Exception,psycopg2.Error) as error:
    print(f'your error is {error}')
  finally:
        if(conn):
          conn.close()
  POSTS.append((content, datetime.datetime.now()))


