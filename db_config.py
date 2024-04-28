
import mysql.connector
from mysql.connector import Error

class DBConfig:
    _instance = None
    
    # Singleton Method
    @staticmethod
    def get_instance():
        if DBConfig._instance is None:
            DBConfig();
        return DBConfig._instance
    #  Singleton Method
    
    def  __init__(self):
        if DBConfig._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DBConfig._instance = self
        self.db_config = {
            'user':'root',
            'password': 'hacha123',
            'host':'localhost',
            'database': 'university'
        }
        
    # def get_db_connected(self):
    #     try :
    #         conn = mysql.connector.connect(**self.db_config)
    #         if conn.is_connected():
    #             print("Connection  succesfull")
    #             return conn
    #         else:
    #             print("connection unsuccessful")
    #     except Error as e:
    #         print(f"Error connecting to MySQL: {e}")
    #         return None
        
if __name__ == "__main__":
    DBConfig().get_db_connected()