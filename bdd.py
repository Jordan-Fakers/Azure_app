import psycopg2
import os
import logging

logging.basicConfig(filename='db_log.txt', level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def connection_db ():
    try:
        print("1")
        
        conn = psycopg2.connect(host= os.getenv('PG_HOST'),
                            user= os.getenv('PG_USER'),
                            database= os.getenv('PG_DATABASE'),
                            password= os.getenv('PG_PASSWORD'))
                                        
        logging.info("[BDD] Successfully connected to your database") 
        return conn
    except Exception as e:
        logging.warning("[BDD] message error:  %s", (e))
    return conn

def select_from_db():
    try:
        co = connection_db()
        cur = co.cursor()
        logging.info("[BDD] flask successfully connected to the databse")
        cur.execute("select * from articles ORDER BY id DESC LIMIT 5")
        results = cur.fetchall()
        logging.info("[FLASK] data successufully fetch from the database")
        return results

    except Exception as e:
        logging.info("[FLASK] fetch of the database failed, error: %s",(e))

        

