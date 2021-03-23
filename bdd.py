import psycopg2

def connection_db ():
    try:
        print("1")
        #J'utilise l'ip public Azure pour me connecter à ma VM et aller sur le PG dessus
        cnx = psycopg2.connect(host= os.getenv('PG_HOST'),
                            user= os.getenv('PG_USER'),
                            database= os.getenv('PG_DATABASE'),
                            password= os.getenv('PG_PASSWORD'))
                                        
        print("Connected to database ")
        logging.info("[FLASK] Successfully connected to your database") 
        return cnx
    except Exception as e:
        logging.warning("[FLASK] message error:  %s", (e))
    return cnx