import psycopg2
import config
from datetime import datetime
import connect

def insertuser(name, password):
    date = datetime.now()
    sql = """INSERT INTO userdb (name,password, date ) VALUES(%s,%s, %s)"""
    connection = None
    try:
        params = config.config()
        connection = connect.connect_dc('connect')
        cur = connection.cursor()
        cur.execute(sql, (name, password, date))
        connection.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print('An Error has been occurs \n',error)
    finally:
        if connection is not None:
            connection.close()
            cur.close()
    return 0
