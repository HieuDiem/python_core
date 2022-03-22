import mysql.connector
class DBProvider:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.passwd = 'root'
        self.db = 'project02db'
        self.conn = None
        self.curr = None
        self.__createDBIfNotExists()

# tao db neu chua ton tai
    def __createDBIfNotExists(self):
        sql = f"CREATE DATABASE IF NOT EXISTS {self.db}"
        # params = (sql.db,)
        conn =  mysql.connector.connect(host=self.host,
                                        user=self.user,
                                        passwd=self.passwd,
                                        )
        curr = conn.cursor()
        curr.execute(sql)
        conn.close()
# ket noi CSDL
    def connect(self):
        self.conn =  mysql.connector.connect(host=self.host,
                                        user=self.user,
                                        passwd=self.passwd,
                                        db=self.db)

        self.curr = self.conn.cursor()
#ngat ket noi CSDL
    def close(self):
        #neu dang ket noi
        if self.conn is not None and self.curr is not None:
            self.conn.close()
            self.conn = None
            self.curr = None

# thuc thi cau lenh sql, dung sua DL: insert/update/del
    def exec(self, sql: str, *params):
        rowCount = 0

        try:
            self.connect()

            self.curr.execute(sql, *params)
            self.conn.commit()
            rowCount = self.curr.rowcount #sl ban ghi bi thay doi
        except Exception as e:
            print(e)
        finally:
            self.close()
        return rowCount
#thuc thi cau lenh sql theo dang truy van DL (nhieu ban ghi): SELECT
    def get(self, sql:str, *params):
        result = [] # result as a list
        try:
            self.connect()

            self.curr.execute(sql, *params)
            result = [row for row in self.curr.fetchall()] #chuyen cac ban ghi vao trg list
            # lst = []
            # for row in self.curr.fetchall():
            #     lst.append(row)
        except Exception as e:
            print(e)
        finally:
            self.close()
        return result
#thuc thi cau lenh sql theo dang truy van DL (1 ban ghi):SELECT
    def getOne(self, sql: str, *params):
        result = None
        try: 
            self.connect()
            self.curr.execute(sql, *params)
            result = self.curr.fetchone() #result as a row
        except:
            print('loi')
        finally:
            self.close()
        return result