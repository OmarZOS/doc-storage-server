
from constants import *
from core.locator import singleton
from storage.storage_service.StorageService import *

import mysql.connector

@singleton
class mysql_wrapper(StorageService):
    
    def __init__(self): # name...,node/edge
        self.mysql_driver = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )

    def _insert(self,table_name,fields,args):
        
        # building the instruction..
        statement = f"INSERT INTO {table_name} {','.join(fields)} VALUES {','.join(x for x in args)}"
        
        # executing the query
        self.mysql_driver.cursor().execute(statement)
        
        self.mysql_driver.cursor().commit()
        
    def _get(self,table_name,fields,conditions):
        # for the sake of simplicity..
        # conditions variable is a pre-built string of AND's
        # conditions = ["field1 = 5","field2 > 3"]
        
        statement = f"SELECT {','.join(fields)} FROM {table_name}" 
        
        if conditions:
            statement +=  f"WHERE {' AND '.join(conditions)}"
            
        self.mysql_driver.cursor().execute(statement)
        
        results = []
        
        for result in self.mysql_driver.cursor():
            results.add(result)
            
        return results
    
    def get(self,table_name,fields,conditions):
        return self._get(self,table_name,fields,conditions)

    def test_connection(self):
        return self.mysql_driver.ping()

    def queryData(self,data):
        # simple direct queries for now..
        return self.get(data["table_name"],data["fields"],data["conditions"])
    
    def saveData(self,data):
        # and pray that it will work..
        self._insert(self,data["table_name"],data["fields"],data["args"])
