import mysql.connector
from mysql.connector import Error

from person_repository import PersonRepository
from db_config import  DBConfig

class PersonRepositoryImpl(PersonRepository):
    
    def __init__(self, db_config):
        self.db_config = db_config
        
    def get_connection(self):
        return mysql.connector.connect(**self.db_config)
    
    
    def add_person(self, person):
        conn = self.get_connection()
        cursor = self.conn.cursor();
        
        try:
            cursor.execute("INSERT INTO persons (id, name) VALUES (%s, %s)", 
                           (person["id"],person['name']))
            conn.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            conn.close()