import pymysql
import traceback
class PyMySQL(object):
    def __init__(self, host, user, pwd):
        self.conn = pymysql.Connect(host=host, user=user, passwd=pwd, charset='utf8')
        self.cursor = self.conn.cursor()

    def change(self, query, args):
        try:
            self.cursor.execute(query, args)
            self.conn.commit()
        except:
            print(traceback.format_exc())
            self.conn.rollback()

    def search(self, query, args):
        self.cursor.execute(query, args)
        results = self.cursor.fetchall()
        return results

    def _quit(self):
        self.cursor.close()
        self.conn.close()