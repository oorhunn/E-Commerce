import psycopg2
import config
from datetime import datetime

def insertuser(name, password):
    date = datetime.now()
    sql = """INSERT INTO userdb (name,password, date ) VALUES(%s,%s, %s)"""
    connection = None
    try:
        params = config.config()
        connection = psycopg2.connect(**params)
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

def insertflask(goldprice, silverprice, copperprice, time):
    sql = """INSERT INTO FlaskOfPower (goldprice,silverprice,copperprice,time) VALUES(%s,%s,%s,%s)"""

    connection = None
    try:
        params = config.config()
        connection = psycopg2.connect(**params)
        cur = connection.cursor()
        cur.execute(sql, (goldprice, silverprice, copperprice, time))
        connection.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            cur.close()
    return 0

# def flasin():
#     FlaskOfPower_price = Request.FlaskOfPower()
#     time = datetime.now()
#     insertflask(FlaskOfPower_price[0], FlaskOfPower_price[1], FlaskOfPower_price[2], time)

insertuser('anil','anan')