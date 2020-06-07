import psycopg2
from time import sleep


class PgConn:
    def __init__(self):
        sleep(10)  # wait for postgres docker
        print("waiting for 10 seconds")
        self.conn = psycopg2.connect(user="postgres",
                                          password="SUPER_SECRET_BRO!",
                                          host="postgres",
                                          database="docker")
        self.pgc = self.conn.cursor()


    def insert_record(self, key, rule, meta):
        postgres_insert_query = """INSERT INTO docker.public.records ("key", "rule", meta) VALUES (%s, %s, %s);"""
        record_to_insert = (key, rule, meta)
        self.pgc.execute(postgres_insert_query, record_to_insert)

        self.conn.commit()

    def check_for_record(self, key):
        try:
            select = """SELECT "key" FROM docker.public.records WHERE "key"=%s;"""

            self.pgc.execute(select, (key,))
            key_exists = self.pgc.fetchall()

            if not key_exists:
                return True
        except Exception:
            return False

        return False

    def close_conn(self):
        self.pgc.close()
        self.conn.close()
