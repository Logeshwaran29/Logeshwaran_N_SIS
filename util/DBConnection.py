import mysql.connector as sql


class DBConnUtil:
    connection = None

    @staticmethod
    def getConnection():
        try:
            connection = sql.connect(host='localhost', database='SISDB', user='root', password='log123@#')
            return connection
        except Exception as e:
            print(e)

