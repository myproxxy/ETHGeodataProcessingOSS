import psycopg2

def postgres_test():

    try:
        conn = psycopg2.connect(dbname="postgis", host="ikgsql2.ethz.ch", user="postgres", password="tur4finupum9", port="5432")
        conn.close()
        return True
    except:
        return False

print(postgres_test())