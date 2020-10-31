import sqlite3


class Connector:

    def __init__(self, db_url):
        conn = sqlite3.connect(db_url)
        self.cursor = conn.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def execute_par(self, query, parameter):
        #self.cursor.execute(query % parameter)
        parameter = ''.join(parameter)
        self.cursor.execute("select count(*) from %s " % ""+"[" + parameter + "]")
        self.cursor.execute(query % ""+"[" + parameter + "]")
        return self.cursor.fetchone()[0]

    def execute_many(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
