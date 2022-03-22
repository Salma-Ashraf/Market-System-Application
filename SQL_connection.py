
def get_sql_connection():
    global __cnx
    import mysql.connector
    __cnx = mysql.connector.connect(user='root', password='Dybala@279090',
                                  host='localhost',
                                  database='grocerry_store')
    return __cnx