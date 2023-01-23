import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()


class DatabaseConfig():
    def __init__(self):
        self.host = os.getenv("host")
        self.user = os.getenv("user")
        self.password = os.getenv("password")
        self.port = os.getenv("port")
        self.connection = None
        self.cursor = None
        self.database_name = None
        self.account_num = 0

    def connect(self):
        self.connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password, port=self.port)
        self.cursor = self.connection.cursor()
        print(f"Connected Successfully")

    def create_database(self, database_name):
        self.cursor.execute(f"DROP DATABASE IF EXISTS {database_name}")
        query = f"CREATE DATABASE {database_name}"
        self.cursor.execute(query)
        print(f"{database_name} created successfully")
        self.database_name = database_name

    def create_table(self, table_name, query):
        self.cursor.execute(f"USE {self.database_name}")
        self.cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        self.cursor.execute(query)
        print(f"{table_name} created successfully")

    def insert_data(self, query, row):
        self.cursor.execute(f"USE {self.database_name}")
        print(self.database_name, query, row)
        self.cursor.execute(query, row)
        self.connection.commit()


    def drop_data(self):
        pass

    def drop_table(self):
        pass

#db_object = DatabaseConfig()
#db_object.connect()
#db_object.create_database("testing")
#query = "CREATE TABLE STUDENT(STUDENT_ID INT NOT NULL PRIMARY KEY, NAME VARCHAR(100), DOB DATE NOT NULL, HEIGHT DECIMAL(4,2))"
#db_object.create_table("Student", query)
#insert_data_queries = ["INSERT INTO STUDENT VALUES(1,'Potato', '2001-12-05', 2.1)","INSERT INTO STUDENT VALUES(2,'Carrot', '2002-12-06', 2.2)" ]
#db_object.insert_data(insert_data_queries)
#db_object.connection.close()

# obj = DatabaseConfig()
# obj.connect("testing")
# insert_data_queries = ['INSERT INTO STUDENT VALUES(4,"Strawberry", "2012-06-09", 4.5), (5,"Strawberry", "2012-06-09", 4.5)']
# obj.insert_data(insert_data_queries)